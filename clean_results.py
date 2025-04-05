import csv
import json
from datetime import datetime

def format_opening_hours(hours_str):
    """Format opening hours from JSON string to readable format"""
    try:
        hours_dict = json.loads(hours_str.replace("'", '"'))
        
        # Check if all days have same hours
        all_hours = [hours_dict[day][0] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] if day in hours_dict and hours_dict[day]]
        
        if len(set(all_hours)) == 1:  # All days same hours
            return f"Mon-Sun: {all_hours[0]}"
        elif len(set(all_hours[:5])) == 1 and len(set(all_hours[5:])) == 1:  # Weekdays same, weekends same
            return f"Mon-Fri: {all_hours[0]}, Sat-Sun: {all_hours[5]}"
        elif len(set(all_hours[:6])) == 1 and all_hours[6] != all_hours[0]:  # Mon-Sat same, Sun different
            return f"Mon-Sat: {all_hours[0]}, Sun: {all_hours[6]}"
        else:
            return ", ".join(f"{day[:3]}: {hours[0]}" for day, hours in hours_dict.items() if hours)
    except:
        return "Not available"

def format_phone(phone):
    """Format phone number consistently"""
    # Remove any spaces or special characters
    phone = ''.join(c for c in phone if c.isdigit())
    
    # Format based on length and prefix
    if len(phone) == 11 and phone.startswith('020'):
        return f"020 {phone[3:7]} {phone[7:]}"
    elif len(phone) == 11 and phone.startswith('033'):
        return f"0333 {phone[4:7]} {phone[7:]}"
    elif len(phone) == 11:
        return f"{phone[:4]} {phone[4:7]} {phone[7:]}"
    else:
        return phone

def clean_address(address):
    """Clean and format address"""
    # Remove duplicate store names in address
    parts = address.split(',')
    cleaned_parts = []
    seen = set()
    for part in parts:
        part = part.strip()
        if part and part not in seen:
            cleaned_parts.append(part)
            seen.add(part)
    return ', '.join(cleaned_parts)

def clean_data():
    with open('results.csv', 'r', encoding='utf-8') as infile, \
         open('cleaned_results.csv', 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = ['Store Name', 'Address', 'Phone Number']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        seen_addresses = set()  # To remove duplicates
        
        for row in reader:
            # Skip if no title, address or phone
            if not row.get('title') or not row.get('address') or not row.get('phone'):
                continue
                
            address = clean_address(row['address'])
            phone = format_phone(row.get('phone', ''))
            
            # Skip if no valid phone number
            if not phone or phone == '':
                continue
                
            # Skip duplicate addresses
            if address in seen_addresses:
                continue
            seen_addresses.add(address)
            
            cleaned_row = {
                'Store Name': row['title'],
                'Address': address,
                'Phone Number': phone
            }
            writer.writerow(cleaned_row)

if __name__ == "__main__":
    clean_data() 
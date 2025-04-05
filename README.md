# Phone Number Scraper

A Python script to extract and clean phone numbers from Google Maps data.

## Features

- Extracts phone numbers from Google Maps scraped data
- Formats UK phone numbers consistently (020, 0333, etc.)
- Removes duplicate entries
- Cleans and validates data
- Outputs clean CSV with store information and phone numbers

## Usage

1. Ensure you have a `results.csv` file with Google Maps scraped data
2. Run the script:
```bash
python3 clean_results.py
```
3. Find the cleaned data in `cleaned_results.csv`

## Output Format

The script outputs a CSV file with three columns:
- Store Name
- Address
- Phone Number

Phone numbers are formatted as:
- 020 numbers: 020 XXXX XXXX
- 0333 numbers: 0333 XXX XXXX
- Other numbers: Standard UK format

## Requirements

- Python 3.x
- CSV module (built-in)
- JSON module (built-in) 
# Product Sales Tracker

A simple Python script that converts product sales data from a text file into an enriched CSV report.

## What it does

- Reads product IDs from `product_sales.txt`
- Looks up product details (name and price) from an internal database
- Creates a CSV file with complete sales information including dates and sale IDs

## Files

- `tracker.py` - Main script
- `product_sales.txt` - Input file with product IDs (one per line)
- `product_sales.csv` - Output CSV file with enriched data

## Output Format

The generated CSV includes these columns:
- **current_date** - Date of processing
- **sale_id** - Sequential sale number
- **product_id** - Product identifier (P001, P002, etc.)
- **name** - Product name
- **price** - Product price

## How to run

```bash
python tracker.py
```

## Supported Products

- P001: Wireless Headphones ($100)
- P002: Laptop Backpack ($60)
- P003: Bluetooth Speaker ($50)
- P004: Laptop Backpack ($20)
- P005: Mobile Phone Case ($15)
- P006: Wireless Mouse ($30)
- P007: Laptop Stand ($40)
- P008: HDMI Cable ($15)
- P009: Smartphone ($600)
- P010: External Hard Drive ($100)

Unknown product IDs will show as "Unknown" with $0 price.
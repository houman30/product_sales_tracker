import datetime
import csv

def link(id):
    device_mapping = {
        'P0001': 'Wireless Headphones',
        'P0002': 'Laptop Backpack',
        'P0003': 'Bluetooth Speaker',
        'P0004': 'Laptop Backpack',
        'P0005': 'Mobile Phone Case',
        'P0006': 'Wireless Mouse',
        'P0007': 'Laptop Stand',
        'P0008': 'HDMI Cable',
        'P0009': 'Smartphone',
        'P0010': 'External Hard Drive'
    }




modified_product_header = []

with open('product_sales.txt', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    headers = next(csv_reader)
    headers.append('rating_category')

    modified_product_header.extend(headers)


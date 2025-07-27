import datetime
import csv

device_mapping = {
    'P0001': {'name': 'Wireless Headphones', 'price': '100'},
    'P0002': {'name': 'Laptop Backpack', 'price': '60'},
    'P0003': {'name': 'Bluetooth Speaker', 'price': '60'},
    'P0004': {'name': 'Laptop Backpack', 'price': '20'},
    'P0005': {'name':'Mobile Phone Case', 'price': '15'},
    'P0006': {'name':'Wireless Mouse', 'price': '30'},
    'P0007': {'name':'Laptop Stand', 'price': '40'},
    'P0008': {'name':'HDMI Cable', 'price': '15'},
    'P0009': {'name':'Smartphone', 'price': '600'},
    'P0010': {'name':'External Hard Drive', 'price': '100'}
}




modified_product_header = []

with open('product_sales.txt', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    headers = next(csv_reader)
    headers.append('rating_category')

    modified_product_header.extend(headers)


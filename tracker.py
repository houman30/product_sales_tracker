import datetime
import csv

def get_product_info(product_id):
    device_mapping = {
        'P001': {'name': 'Wireless Headphones', 'price': '100'},
        'P002': {'name': 'Laptop Backpack', 'price': '60'},
        'P003': {'name': 'Bluetooth Speaker', 'price': '50'},
        'P004': {'name': 'Laptop Backpack', 'price': '20'},
        'P005': {'name':'Mobile Phone Case', 'price': '15'},
        'P006': {'name':'Wireless Mouse', 'price': '30'},
        'P007': {'name':'Laptop Stand', 'price': '40'},
        'P008': {'name':'HDMI Cable', 'price': '15'},
        'P009': {'name':'Smartphone', 'price': '600'},
        'P010': {'name':'External Hard Drive', 'price': '100'}
}

    return device_mapping.get(product_id, {'name': 'Unknown', 'price': '0'})



modified_product_header = []
with open('product_sales.txt', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    headers = ['current_date', 'sale_id', 'product_id', 'name', 'price', 'total_revenue']


    modified_product_header.append(headers)

    sale_id = 0
    for row in csv_reader:
        sale_id += 1
        product_info = get_product_info(row[0])

        new_row = [
            datetime.date.today(),
            sale_id,
            row[0],
            product_info['name'],
            product_info['price'],
            int(product_info['price'])
        ]
        modified_product_header.append(new_row)

with open('product_sales.csv', 'w', newline='') as new_csv_file:

    csv_writer = csv.writer(new_csv_file)

    csv_writer.writerows(modified_product_header)
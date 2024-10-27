import random
from prettytable import PrettyTable
from login import validation
from products import purchase
products = [
    {"Name": "Water", "Price": 80.0, "Quantity": 1200},
    {"Name": "Soda", "Price": 130.0, "Quantity": 1200},
    {"Name": "Chips", "Price": 75.0, "Quantity": 1200},
    {"Name": "Bread", "Price": 45.0, "Quantity": 1200},
    {"Name": "Eggs", "Price": 65.0, "Quantity": 1200}
]

table = PrettyTable()
table.field_names  = ['Name','Price','Quantity']
for i in products:
    table.add_row([i['Name'],i['Price'],i['Quantity']])
print(table)
total_discount = 0 
validation()
purchase(products)

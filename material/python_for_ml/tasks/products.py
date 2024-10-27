
def purchase(products):
    while True:
        product_name = input('enter product name: ').lower()
        if product_name not in map(lambda x: x['Name'].lower(),products):
            print('product not found in the table. please enter a valid product')
            continue
        quantity_required = float(input('enter quantity required: '))
        product = next(p for p in products if p['Name'].lower()==product_name)
        if quantity_required > product['Quantity']:
            print('insuffient quntity. please enter a new quantity')
            continue
        break
    total_discount = min(quantity_required // 50, 25.0)  # Cap the discount at 25%
    discounted_price = quantity_required * product["Price"] * (1 - total_discount / 100)
    print(discounted_price)
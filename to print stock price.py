inventory=[
    ("laptop",5,30000.00),
    ("headphone",15,500.00),
    ("mouse",50,150.00),
    ("keyboard",20,150.00),
    ("monitor",10,3000)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price=item
    stock_value=quantity*unit_price
    print(f"Item name:{item_name},the stock value is: {stock_value}")
    if stock_value > highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
print(f"Highest stock value is:{highest_stock_value}")
print(f"Item with highest stock value is:{item_with_highest_stock_value}")


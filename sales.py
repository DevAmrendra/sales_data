sales_data = [
    {"product": "Laptop", "price": 900, "quantity_sold": 5, "total_revenue": 4500},
    {"product": "Smartphone", "price": 600, "quantity_sold": 8, "total_revenue": 4800},
    {"product": "Tablet", "price": 300, "quantity_sold": 10, "total_revenue": 3000},
    {"product": "Headphones", "price": 150, "quantity_sold": 20, "total_revenue": 3000},
    {"product": "Smartwatch", "price": 200, "quantity_sold": 12, "total_revenue": 2400},
    {"product": "Camera", "price": 800, "quantity_sold": 3, "total_revenue": 2400},
    {"product": "Printer", "price": 250, "quantity_sold": 6, "total_revenue": 1500},
    {"product": "Monitor", "price": 350, "quantity_sold": 7, "total_revenue": 2450},
    {"product": "Keyboard", "price": 50, "quantity_sold": 30, "total_revenue": 1500},
    {"product": "Mouse", "price": 30, "quantity_sold": 40, "total_revenue": 1200}
]

net_revenue = 0
more_than_500_in_price = 0
highest_revenue_product = sorted(sales_data, key=lambda x: x["total_revenue"], reverse = True)

for i in sales_data:
    net_revenue = net_revenue + i["total_revenue"]

for i in sales_data:
    if i["price"] > 500:
        more_than_500_in_price+=1

print(net_revenue)
print(highest_revenue_product[0]["product"])
print(more_than_500_in_price)
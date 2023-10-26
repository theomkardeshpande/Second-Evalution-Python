import pandas as pd
import matplotlib.pyplot as plt

class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        self.inventory[item_name] = {"quantity": quantity, "price": price}

    def update_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            self.inventory[item_name]["quantity"] = quantity
            self.inventory[item_name]["price"] = price

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]

    def generate_report(self):
        print("Inventory Report:")
        for item_name, item_info in self.inventory.items():
            print(f"Item: {item_name}, Quantity: {item_info['quantity']}, Price: {item_info['price']}")

# Example usage
inventory = Inventory()
inventory.add_item("Product A", 100, 10.99)
inventory.add_item("Product B", 50, 5.99)
inventory.update_item("Product A", 80, 9.99)
inventory.remove_item("Product B")
inventory.generate_report()

class SalesDatabase:
    def __init__(self):
        self.sales_data = []

    def record_sale(self, customer_name, items_purchased, total_amount):
        sale_record = {"customer_name": customer_name, "items_purchased": items_purchased, "total_amount": total_amount}
        self.sales_data.append(sale_record)

    def calculate_total_sales(self, period_start, period_end):
        total_sales = 0
        for sale in self.sales_data:
            if period_start <= sale["date"] <= period_end:
                total_sales += sale["total_amount"]
        return total_sales

    def provide_discount(self, customer_name, discount_percentage):
        for sale in self.sales_data:
            if sale["customer_name"] == customer_name:
                sale["total_amount"] *= (1 - discount_percentage / 100)

    def generate_sales_report(self):
        print("Sales Report:")
        for sale in self.sales_data:
            print(f"Customer: {sale['customer_name']}, Total Amount: {sale['total_amount']}")

# Example usage
sales_db = SalesDatabase()
sales_db.record_sale("Customer 1", ["Product A", "Product B"], 15.99)
sales_db.record_sale("Customer 2", ["Product A"], 9.99)
sales_db.provide_discount("Customer 1", 10)
sales_db.generate_sales_report()


# Assuming you have a CSV file with sales data
sales_data = pd.read_csv("sales_data.csv")

# Analyze sales trends over time
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data.set_index('Date', inplace=True)

# Create a sales chart
plt.figure(figsize=(10, 6))
sales_data['Sales'].plot(title='Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Identify peak sales hours and popular products
peak_hours = sales_data.groupby(sales_data.index.hour)['Sales'].sum()
popular_products = sales_data['Product'].value_counts()

# Generate reports for store management
print("Peak Sales Hours:")
print(peak_hours)

print("\nPopular Products:")
print(popular_products)


from src.data.loader import load_orders, load_products, load_customers

orders = load_orders()
products = load_products()
customers = load_customers()

print("Orders:", orders.shape)
print("Products:", products.shape)
print("Customers:", customers.shape)

print("\nFirst 5 orders:")
print(orders.head())

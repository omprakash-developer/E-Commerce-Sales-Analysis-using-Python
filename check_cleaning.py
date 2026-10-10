
from src.data.loader import load_orders
from src.data.validator import validate_orders
from src.data.cleaner import clean_orders, save_cleaned_data

orders = load_orders()

print("===== VALIDATION REPORT =====")
for key, value in validate_orders(orders).items():
    print(f"{key}: {value}")

cleaned = clean_orders(orders)
save_cleaned_data(cleaned)

print("\n===== CLEANING REPORT =====")
print("Rows before cleaning:", len(orders))
print("Rows after cleaning:", len(cleaned))
print("Saved to data/processed/cleaned_sales.csv")

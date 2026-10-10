
from src.data.loader import load_orders
from src.data.cleaner import clean_orders
from src.analysis.sales_analysis import (
    get_total_sales,
    get_total_profit,
    get_total_orders,
    get_total_quantity,
    get_average_order_value,
    get_profit_margin,
    get_monthly_sales,
    get_sales_by_region,
)


def main():
    orders = clean_orders(load_orders())

    print("\n===== SALES OVERVIEW =====")
    print(f"Total Revenue: ₹{get_total_sales(orders):,.2f}")
    print(f"Total Profit: ₹{get_total_profit(orders):,.2f}")
    print(f"Total Orders: {get_total_orders(orders)}")
    print(f"Units Sold: {get_total_quantity(orders)}")
    print(f"Average Order Value: ₹{get_average_order_value(orders):,.2f}")
    print(f"Profit Margin: {get_profit_margin(orders):.2f}%")

    print("\n===== MONTHLY SALES =====")
    print(get_monthly_sales(orders).to_string(index=False))

    print("\n===== REGIONAL SALES =====")
    print(get_sales_by_region(orders).to_string(index=False))


if __name__ == "__main__":
    main()

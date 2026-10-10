
import pandas as pd


REQUIRED_COLUMNS = [
    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Product_ID",
    "Quantity",
    "Unit_Price",
    "Discount",
    "Sales",
    "Profit",
    "Payment_Method",
    "Region",
    "City",
]


def validate_orders(df: pd.DataFrame) -> dict:
    """Check the quality of the orders dataset."""

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        return {
            "total_rows": len(df),
            "missing_columns": missing_columns,
            "duplicate_rows": None,
            "missing_values": None,
            "invalid_quantity_rows": None,
            "invalid_price_rows": None,
            "invalid_discount_rows": None,
        }

    quantity = pd.to_numeric(df["Quantity"], errors="coerce")
    price = pd.to_numeric(df["Unit_Price"], errors="coerce")
    discount = pd.to_numeric(df["Discount"], errors="coerce")

    return {
        "total_rows": len(df),
        "missing_columns": [],
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": int(df[REQUIRED_COLUMNS].isna().sum().sum()),
        "invalid_quantity_rows": int(
            (quantity.isna() | (quantity <= 0)).sum()
        ),
        "invalid_price_rows": int(
            (price.isna() | (price < 0)).sum()
        ),
        "invalid_discount_rows": int(
            (discount.isna() | ~discount.between(0, 1)).sum()
        ),
    }

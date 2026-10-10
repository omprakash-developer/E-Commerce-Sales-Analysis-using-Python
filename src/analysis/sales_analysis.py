
import pandas as pd


def get_total_sales(df: pd.DataFrame) -> float:
    """Calculate total revenue."""
    return float(df["Sales"].sum())


def get_total_profit(df: pd.DataFrame) -> float:
    """Calculate total profit."""
    return float(df["Profit"].sum())


def get_total_orders(df: pd.DataFrame) -> int:
    """Count unique orders."""
    return int(df["Order_ID"].nunique())


def get_total_quantity(df: pd.DataFrame) -> int:
    """Calculate total units sold."""
    return int(df["Quantity"].sum())


def get_average_order_value(df: pd.DataFrame) -> float:
    """Calculate average revenue per unique order."""
    total_orders = get_total_orders(df)

    if total_orders == 0:
        return 0.0

    return get_total_sales(df) / total_orders


def get_profit_margin(df: pd.DataFrame) -> float:
    """Calculate profit as a percentage of revenue."""
    total_sales = get_total_sales(df)

    if total_sales == 0:
        return 0.0

    return (get_total_profit(df) / total_sales) * 100


def get_monthly_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize sales, profit and orders by month."""
    data = df.copy()

    data["Order_Date"] = pd.to_datetime(
        data["Order_Date"], errors="coerce"
    )

    data = data.dropna(subset=["Order_Date"])
    data["Month"] = data["Order_Date"].dt.to_period("M").astype(str)

    result = (
        data.groupby("Month", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order_ID", "nunique"),
        )
        .sort_values("Month")
        .reset_index(drop=True)
    )

    return result


def get_sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize sales, profit and orders by region."""
    result = (
        df.groupby("Region", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order_ID", "nunique"),
        )
        .sort_values("Sales", ascending=False)
        .reset_index(drop=True)
    )

    return result

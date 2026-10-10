
import pandas as pd

from src.data.validator import REQUIRED_COLUMNS


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare orders data for analysis."""

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    df = df.copy()

    df = df.drop_duplicates()

    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"], errors="coerce"
    )

    numeric_columns = [
        "Quantity", "Unit_Price", "Discount", "Sales", "Profit"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

    df = df.dropna(subset=REQUIRED_COLUMNS)

    df = df[
        (df["Quantity"] > 0)
        & (df["Unit_Price"] >= 0)
        & (df["Discount"].between(0, 1))
        & (df["Sales"] >= 0)
        & (df["Profit"] >= 0)
    ]

    for column in ["Order_ID", "Customer_ID", "Product_ID"]:
        df = df[
            df[column].astype(str).str.strip().ne("")
        ]

    return df.reset_index(drop=True)


def save_cleaned_data(
    df: pd.DataFrame,
    output_path: str = "data/processed/cleaned_sales.csv",
) -> None:
    from pathlib import Path

    path = Path(output_path)

    if not path.is_absolute():
        path = Path(__file__).resolve().parents[2] / path

    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)

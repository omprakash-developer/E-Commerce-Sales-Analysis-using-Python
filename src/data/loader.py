
from pathlib import Path

import pandas as pd


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def load_csv(filename: str) -> pd.DataFrame:
    """Load a CSV file from the raw data directory."""
    file_path = RAW_DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    return pd.read_csv(file_path)


def load_orders() -> pd.DataFrame:
    return load_csv("orders.csv")


def load_products() -> pd.DataFrame:
    return load_csv("products.csv")


def load_customers() -> pd.DataFrame:
    return load_csv("customers.csv")

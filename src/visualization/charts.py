
import matplotlib.pyplot as plt
import pandas as pd


def monthly_sales_chart(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(
        df["Month"],
        df["Sales"],
        marker="o",
        linewidth=2,
        label="Revenue",
    )

    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue (INR)")
    ax.grid(axis="y", alpha=0.3)
    ax.legend()
    fig.tight_layout()

    return fig


def regional_sales_chart(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(df["Region"], df["Sales"])

    ax.set_title("Revenue by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Revenue (INR)")
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()

    return fig


def category_sales_chart(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(df["Category"], df["Revenue"])
    ax.set_title("Revenue by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue (INR)")
    ax.tick_params(axis="x", rotation=15)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()

    return fig


def top_products_chart(df: pd.DataFrame):
    top = df.nlargest(5, "Revenue").sort_values("Revenue")

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.barh(top["Product_Name"], top["Revenue"])
    ax.set_title("Top 5 Products by Revenue")
    ax.set_xlabel("Revenue (INR)")
    ax.set_ylabel("Product")
    ax.grid(axis="x", alpha=0.3)
    fig.tight_layout()

    return fig

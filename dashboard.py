
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.data.loader import load_orders, load_products
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

from src.visualization.charts import (
    monthly_sales_chart,
    regional_sales_chart,
    category_sales_chart,
    top_products_chart,
)


st.set_page_config(
    page_title="E-Commerce Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("📊 E-Commerce Sales Analytics")
st.caption("Python • Pandas • Matplotlib | Sample Dataset: Jan–Mar 2026")

# Load and clean data
try:
    orders = clean_orders(load_orders())
    products = load_products()
except Exception as error:
    st.error(f"Unable to load data: {error}")
    st.stop()

# Connect orders with product details
data = orders.merge(
    products[["Product_ID", "Product_Name", "Category"]],
    on="Product_ID",
    how="left",
    validate="many_to_one",
)

if data["Product_Name"].isna().any():
    st.error("Some orders do not match a product in products.csv.")
    st.stop()

# Sidebar filter
st.sidebar.header("Dashboard Filters")

regions = sorted(data["Region"].dropna().unique().tolist())

selected_regions = st.sidebar.multiselect(
    "Select regions",
    options=regions,
    default=regions,
)

if not selected_regions:
    st.warning("Select at least one region to view analytics.")
    st.stop()

filtered = data[data["Region"].isin(selected_regions)].copy()

st.sidebar.caption(f"Showing {len(filtered)} order records")
st.caption(
    "Selected regions: " + ", ".join(selected_regions)
)

# KPI cards
st.subheader("Business Overview")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Revenue", f"₹{get_total_sales(filtered):,.0f}")
k2.metric("Total Profit*", f"₹{get_total_profit(filtered):,.0f}")
k3.metric("Total Orders", f"{get_total_orders(filtered):,}")
k4.metric("Units Sold", f"{get_total_quantity(filtered):,}")

k5, k6 = st.columns(2)

k5.metric(
    "Average Order Value",
    f"₹{get_average_order_value(filtered):,.2f}",
)
k6.metric(
    "Profit Margin*",
    f"{get_profit_margin(filtered):.2f}%",
)

st.divider()

# Monthly and regional charts
left, right = st.columns(2)

with left:
    st.subheader("Monthly Sales Trend")
    monthly = get_monthly_sales(filtered)
    fig = monthly_sales_chart(monthly)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

with right:
    st.subheader("Regional Performance")
    regional = get_sales_by_region(filtered)
    fig = regional_sales_chart(regional)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

st.divider()

# Category and product charts
category_data = (
    filtered.groupby("Category", as_index=False)
    .agg(
        Revenue=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum"),
    )
    .sort_values("Revenue", ascending=False)
)

product_data = (
    filtered.groupby(
        ["Product_ID", "Product_Name"], as_index=False
    )
    .agg(
        Revenue=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum"),
        Orders=("Order_ID", "nunique"),
    )
)

left, right = st.columns(2)

with left:
    st.subheader("Category Performance")
    fig = category_sales_chart(category_data)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

with right:
    st.subheader("Top 5 Products")
    fig = top_products_chart(product_data)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

# Data tables
with st.expander("View Monthly Sales Data"):
    st.dataframe(monthly, use_container_width=True)

with st.expander("View Product Performance"):
    st.dataframe(
        product_data.sort_values("Revenue", ascending=False),
        use_container_width=True,
    )

with st.expander("View Category Performance"):
    st.dataframe(category_data, use_container_width=True)

st.caption(
    "*Profit and margin use the sample Profit column and "
    "have not yet been reconciled with product costs and discounts."
)
st.caption("Educational project demo. Results are based on sample CSV data.")

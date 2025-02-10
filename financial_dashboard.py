import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Set up the page layout
st.set_page_config(page_title="Financial Reporting Dashboard", layout="wide")

# Dummy data for financial metrics
def generate_sample_data():
    metrics = {
        "Revenue": 1000000,
        "Expenses": 750000,
        "Profit": 250000,
        "Profit Margin (%)": round((250000 / 1000000) * 100, 2),
    }
    return metrics

# Dummy data for trends and tables
def generate_trend_data():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    revenue = [80000, 85000, 90000, 95000, 100000, 110000, 120000, 125000, 130000, 140000, 150000, 160000]
    expenses = [70000, 72000, 75000, 78000, 80000, 85000, 88000, 90000, 95000, 100000, 105000, 110000]
    return pd.DataFrame({"Month": months, "Revenue": revenue, "Expenses": expenses})

def generate_table_data():
    data = {
        "Category": ["Salaries", "Marketing", "Operations", "Technology", "Miscellaneous"],
        "Amount": [300000, 150000, 200000, 80000, 20000],
    }
    return pd.DataFrame(data)

# Main application function
def main():
    st.title("📊 Financial Reporting Dashboard")
    st.write("Welcome to the Financial Reporting Dashboard. This template allows you to monitor key financial metrics, trends, and expenses.")

    # Metrics section
    st.subheader("Key Financial Metrics")
    metrics = generate_sample_data()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💰 Revenue", f"${metrics['Revenue']:,}")
    col2.metric("📉 Expenses", f"${metrics['Expenses']:,}")
    col3.metric("📈 Profit", f"${metrics['Profit']:,}")
    col4.metric("📊 Profit Margin (%)", f"{metrics['Profit Margin (%)']}%")

    # Trends section
    st.subheader("📈 Financial Trends")
    trend_data = generate_trend_data()

    # Line chart: Revenue vs Expenses
    fig = px.line(trend_data, x="Month", y=["Revenue", "Expenses"], markers=True, title="Monthly Revenue vs Expenses")
    st.plotly_chart(fig, use_container_width=True)

    # Expenses breakdown
    st.subheader("📂 Expenses Breakdown")
    table_data = generate_table_data()

    col_pie, col_table = st.columns([1, 1])
    with col_pie:
        # Pie chart: Expense categories
        fig_pie = px.pie(table_data, values="Amount", names="Category", title="Expense Categories")
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_table:
        # Expense table
        st.write("### Expense Details")
        st.dataframe(table_data.style.format({"Amount": "${:,.2f}"}), height=300)

    # Add a sidebar
    st.sidebar.title("📊 Filters")
    st.sidebar.markdown("Customize your financial dashboard:")
    date_range = st.sidebar.date_input("Select Date Range", [])
    category_filter = st.sidebar.multiselect("Filter by Category", options=table_data["Category"].tolist())
    st.sidebar.markdown("Built with ❤️ using Streamlit.")

    # Conditional filtering for data
    if category_filter:
        filtered_data = table_data[table_data["Category"].isin(category_filter)]
        st.write("### Filtered Expense Details")
        st.dataframe(filtered_data.style.format({"Amount": "${:,.2f}"}))

# Run the dashboard
if __name__ == "__main__":
    main()

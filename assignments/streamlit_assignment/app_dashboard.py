import streamlit as st

# Title and Description
st.title("Simple Sales Dashboard")
st.write("Track monthly sales performance")

# Months selectbox
months = ["January", "February", "March", "April"]
selected_month = st.selectbox("Select a Month", months)

# Month-wise sales data
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

# Display selected month's sales
st.subheader(f"Sales for {selected_month}")
st.metric("Total Sales", f"${sales[selected_month]}")

# Display bar chart with month labels
st.subheader("Monthly Sales Overview")
st.bar_chart(sales)
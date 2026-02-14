import streamlit as st

# Add user inputs in Sidebar
product_name = st.sidebar.text_input("Enter Product name")
category = st.sidebar.selectbox("Select Category", options=['Laptops', 'Mobiles', 'Accessories', 'Headphones', 'Others'])
price = st.sidebar.number_input("Enter Price")

# Display all Product Inputs
if st.sidebar.button("Add Product"):
    st.success("Products added Successfully!") # Shows Success Message
    st.write("Product name:",product_name)
    st.write("Category:", category)
    st.write("Price:",price)

import streamlit as st

# Enter product price and discount percentage
price = float(st.number_input("Enter Price"))
discount = float(st.slider("Discount Percentage", min_value=0, max_value=50))

# Apply discount when  button is clicked
if st.button("Calculate discount"):
    discounted_price = price - price*discount/100
    st.success("Success!") # Show success message
    data = [['Before', 'After'],[price, discounted_price]]
    st.table(data, border=True)
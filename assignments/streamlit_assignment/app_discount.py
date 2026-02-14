import streamlit as st

price = float(st.number_input("Enter Price"))
discount = float(st.slider("Discount Percentage", min_value=0, max_value=50))

if st.button("Calculate discount"):
    discounted_price = price - price*discount/100
    st.success("Success!")
    data = [['Before', 'After'],[price, discounted_price]]
    st.table(data, border=True)
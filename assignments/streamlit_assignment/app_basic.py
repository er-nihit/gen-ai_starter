
import streamlit as st

st.title("Welcome to Streamlit")
name = st.text_input("")
if st.button("Greet Me"):
    st.write(f"Hello, {name}!")
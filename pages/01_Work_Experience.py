import streamlit as st

st.write("Hello, Streamlit!")

x = st.text_input("Enter your name:", key="name_input")

st.write(f"Hello, {x}!")
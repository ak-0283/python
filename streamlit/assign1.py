import streamlit as st

st.title("Programming Language Picker")
st.text("Assignment 01")

lang = st.selectbox("Your fav language:", ["Python","Java","C++","C","MYSQL","Javascipt"])
st.success(f"Your choose {lang}. Excellent Choice")
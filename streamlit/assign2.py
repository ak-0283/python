import streamlit as st
from datetime import date


st.title("Find Your Age Calculator")
st.text("Assignment 02")

today = date.today()


name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name}! Let's calculate your age")


dob = st.date_input(
    "Enter your date of birth:",
    min_value=date(1900, 1, 1),   
    max_value=today
)


if st.button("Calculate Age"):
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.success(f"Your age is: {age} years")
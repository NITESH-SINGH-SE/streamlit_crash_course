import streamlit as st
from datetime import date

st.title("Age Calculator")

name = st.text_input("Enter your name: ")
dob = st.date_input("Enter your age: ", value=None)
today = date.today()

if dob:
    st.write(f"Hi {name}! You were born in {dob}")
    st.write(f"Current Year {today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))}")
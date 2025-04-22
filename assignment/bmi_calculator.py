import streamlit as st

st.title("BMI Calculator")

height = st.number_input("Enter your height in cm", value=None)
weight = st.number_input("Enter your weight in kg", value=None)

if height and weight:
    bmi = weight / ((height/100) * (height/100))
    message = f"Your bmi is {bmi}"
    if bmi > 25 or bmi < 18:
        st.warning(message)
    else:
        st.success(message)
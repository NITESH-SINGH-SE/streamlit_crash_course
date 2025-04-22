import streamlit as st
import requests

st.title("Weather App")

city = st.text_input("Enter your city: ")
generate = st.button("Check Weather")

if generate:
    response = requests.get(f'https://wttr.in/{city}?format=%C+%t')
    if response.status_code == 200:
        st.write(f"The weather in {city} is {response.text}")
    else:
        st.error("Unable to fetch data.")
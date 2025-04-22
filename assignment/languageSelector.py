import streamlit as st

st.title("Language selector")

language = st.selectbox("Select Language", ["C", "C++", "JavaScript", "Python"], placeholder="Select", index = None)

if language:
    st.write(f"You selected {language}, great choice!")
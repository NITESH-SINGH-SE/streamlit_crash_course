import streamlit as st
import pandas as pd

df = pd.read_csv('Chocolate Sales.csv')

st.title("Data Analysis")
st.table(df.head())

st.write(df.shape)
st.write(df.describe())


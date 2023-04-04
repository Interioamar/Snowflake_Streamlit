#this is the main file
import streamlit as st
import numpy as np
import pandas as pd
st.title("New Healthy Diner")

st.header('Breakfast Menu')
st.text(' 🐔 Omega 3 & Blueberry Oatmeal')
st.text('😀 ale, Spinach & Rocket Smoothie')
st.text('🍐 Like a Hard-Boiled Free-Range Egg')

st.header('🍌🍋 Build Your Own Fruit Smoothie  🍇🐔')

list1=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
st.dataframe(list1)

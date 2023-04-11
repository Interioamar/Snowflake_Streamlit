#this is the main file
import streamlit as st
import numpy as np
import pandas as pd
import requests  #get an API call
st.title("My New Healthy Diner")

st.header('Breakfast Menu')
st.text(' 🐔 Omega 3 & Blueberry Oatmeal')
st.text('😀 ale, Spinach & Rocket Smoothie')
st.text('🍐 Like a Hard-Boiled Free-Range Egg')

st.header('🍌🍋 Build Your Own Fruit Smoothie  🍇🐔')

my_fruit_list=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

my_fruit_list=my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Banana'])
st.dataframe(fruits_selected)
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)

st.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json())


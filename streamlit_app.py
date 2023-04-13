#this is the main file
import streamlit as st
import numpy as np
import pandas as pd
import requests  #get an API call
import snowflake.connector
import streamlit
from urllib.error import URLError

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

st.header("Fruityvice Fruit Advice!") #adds a header
def fruitvice_data(fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice) #gets the request data through URL
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json()) #json_normalize
  return fruityvice_normalized

try:
  fruit_choice = st.text_input('What fruit would you like information about?') #creates an input box for fruits with default value as kiwi
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    st.write('The user entered ', fruit_choice) #creates an text with The user entered Kiwi/input
    get_fruit_function_data=fruitvice_data(fruit_choice)
    st.dataframe(get_fruit_function_data) #displaying in dataframe 
except URLError as e:
  streamlit.error()

st.header("The fruit load list contains")
def get_full_fruits_load():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()

#Adding button to load the fruit
if st.button('Get_fruit_list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_full_fruits_load()
  st.dataframe(my_data_row)

streamlit.stop()
fruit_choice = st.text_input('What fruit would you like to add','jackfruit') #creates an input box for fruits with default value as kiwi
st.write('Thanks for adding ', fruit_choice) #creates an text with The user entered Kiwi/input
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('from_streamlit')")


#this is the main file
import streamlit as st
import numpy as np
import pandas as pd
import requests  #get an API call
import snowflake.connector

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

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi') #creates an input box for fruits with default value as kiwi
st.write('The user entered ', fruit_choice) #creates an text with The user entered Kiwi/input

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice) #gets the request data through URL
## st.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json()) #json_normalize -->> normalizes the json data into flat table
st.dataframe(fruityvice_normalized) #displaying in dataframe 

import streamlit
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('from_streamlit')")
my_data_row = my_cur.fetchall()
st.text("The fruit load list contains")
st.dataframe(my_data_row)

fruit_choice = st.text_input('What fruit would you like to add','jackfruit') #creates an input box for fruits with default value as kiwi
st.write('Thanks for adding ', fruit_choice) #creates an text with The user entered Kiwi/input







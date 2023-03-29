import streamlit
import pandas 
import requests

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = fruits_to_show.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(fruits_to_show.index))
fruits_to_show = fruits_selected.loc[fruits_selected]


# streamlit.dataframe(fruits_to_show)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response.json())

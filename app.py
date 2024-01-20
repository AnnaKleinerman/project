import pandas as pd

data=pd.read_csv('vehicles_us.csv')
data.head()

import streamlit as st
import plotly.express as px

import altair as al

data=pd.read_csv('vehicles_us.csv')
st.title('What is your dream car?')
st.subheader('We have the best prices, the best cars just use this app to select your future car ')

import urllib.request
from PIL import Image

urllib.request.urlretrieve(
  'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bentleymotors.com%2Fen.html&psig=AOvVaw1d5joONWXm3JripboE3npc&ust=1705864416568000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCMCDuK3W7IMDFQAAAAAdAAAAABAD')
  
img = Image.open("gfg.png")

st.image(img)

st.caption(':red[Choose your parameters here]')

price_range = st.slider(
     "What is your price range?",
     value=(1100, 375000))

actual_range=list(range(price_range[0],price_range[1]+1))

model_year = st.checkbox('model_year')

if model_year:
    filtered_data=data[data.price.isin(actual_range)]
    filtered_data=filtered_data[data.rating>=2018]
else:
    filtered_data=data[data.price.isin(actual_range)]


st.write('Here are your options with a split by Price and Model year')

fig = px.scatter(filtered_data, x="price", y="model_year")           
st.plotly_chart(fig)

st.write('Distribution of price')
fig2 = px.histogram(filtered_data, x="price")
st.plotly_chart(fig2)


st.write('Here is the list of latest date_posted ad')
st.dataframe(filtered_data.sample(20))



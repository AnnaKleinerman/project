import pandas as pd

data=pd.read_csv('vehicles_us.csv')
data.head()

import streamlit as st
import plotly.express as px

import altair as al

data=pd.read_csv('vehicles_us.csv')
st.title('What is your dream car?')
st.subheader('We have the best prices, the best cars! just use this app to select your future car ')

import urllib.request
from PIL import Image

urllib.request.urlretrieve(
  'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bentleymotors.com%2Fen.html&psig=AOvVaw1d5joONWXm3JripboE3npc&ust=1705864416568000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCMCDuK3W7IMDFQAAAAAdAAAAABAD')
  
img = Image.open("gfg.png")

st.image(img)
st.caption(':blue[Choose your parameters here]')


price_range = st.slider(
     "What is your price range?",
     value=(1100, 375000))

actual_range=list(range(price_range[0],price_range[1]+1))


transmission_manual = st.checkbox('Manual Transmission')
transmission_automatic = st.checkbox('Automatic Transmission')
transmission_other = st.checkbox('Other Transmission')


filtered_data = data[data.price.isin(actual_range)]

if transmission_manual:
    filtered_data = filtered_data[filtered_data.transmission == 'manual']

if transmission_automatic:
    filtered_data = filtered_data[filtered_data.transmission == 'automatic']

if transmission_other:
    filtered_data = filtered_data[filtered_data.transmission == 'other']


st.write("Filtered Data:")
st.write(filtered_data)


st.write('Here are your options with a split by Fule type and Model year')

fig = px.scatter(filtered_data, x="price", y="model_year")           
st.plotly_chart(fig)

st.write('Distribution of fule')
fig2 = px.histogram(filtered_data, x="fule", y="price")
st.plotly_chart(fig2)


st.write('Here are your options with a split by Transmission ans days listed')

fig = px.histogram(filtered_data, x="transmission", y="days_listed")           
st.plotly_chart(fig)

fig = px.scatter(filtered_data, x="price", y="condition")           
st.plotly_chart(fig)


import pandas as pd

data=pd.read_csv('vehicles_us.csv')
data.head()

import streamlit as st
import plotly.express as px

import altair as al

data=pd.read_csv('vehicles_us.csv')
st.title('Choose your car!')
st.subheader('Use this app to select your future car ')

import urllib.request
from PIL import Image

urllib.request.urlretrieve(
  'https://i.insider.com/5fc8202350e71a001155892f?width=700')
  
img = Image.open("gfg.png")

st.image(img)

st.caption(':red[Choose your parameters here]')

price_range = st.slider(
     "What is your price range?",
     value=(1100, 375000))

actual_range=list(range(price_range[0],price_range[1]+1))

high_rating = st.checkbox('model_year')

if high_rating:
    filtered_data=data[data.price.isin(actual_range)]
    filtered_data=filtered_data[data.rating>=2010]
else:
    filtered_data=data[data.price.isin(actual_range)]


st.write('Here are your options with a split by price and model_year')

fig = px.scatter(filtered_data, x="price", y="model_year")           
st.plotly_chart(fig)

st.write('Distribution of conditions')
fig2 = px.histogram(filtered_data, x="condition")
st.plotly_chart(fig2)


st.write('Here is the list of new condition cars')
st.dataframe(filtered_data.sample(40))



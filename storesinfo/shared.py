from random import randint
from django.db import models
from msilib.schema import Class
import pandas as pd
import plotly.express as px

def generateID():
  letters = 'XX'
  value = randint(1000, 9999)
  return letters+value

def dataToDataframe(data):
  keys = ['Store Code', 'Name', 'City', 'Country', 'Longitude', 'Latitude']
  store_code = []
  name = []
  city = []
  country = []
  longitude = []
  latitude = []
  for i in data:
    store_code.append(i.store_code)
    name.append(i.name)
    city.append(i.city)
    country.append(i.country)
    longitude.append(i.longitude)
    latitude.append(i.latitude)

  frame = pd.DataFrame({
      keys[0]: store_code,
      keys[1]: name,
      keys[2]: city,
      keys[3]: country,
      keys[4]: longitude,
      keys[5]: latitude})

  html_frame = frame.to_html(classes = 'table table-hover dataframe').replace('border="1"','border="0"')
  return html_frame

def displayBarChart(data, chartTitle, xlabel, ylabel):
  fig = px.bar(
    x=[item.country for item in data],
    y=[item.amountStores for item in data],
    text_auto='.2s',
    title=chartTitle,
    labels={'x':xlabel, 'y': ylabel}
  )
  fig.update_traces(textfont_size=27, textangle=0, textposition="outside", cliponaxis=False)
  fig.update_layout(paper_bgcolor='rgba(0, 0, 0, 0)')

  chart = fig.to_html()
  return {'chart':chart}


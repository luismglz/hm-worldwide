from random import randint
from django.db import models
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

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
  fig.update_layout(paper_bgcolor='rgba(0, 0, 0, 0)', font_size=14, font_color='white')

  chart = fig.to_html()
  return chart


def displayPieChart(data, country):
  fig = px.pie(data, values=[item.amount for item in data], names=[item.city for item in data],
              title= f'Top 5 cities with the most stores ({country})', labels={'amount':'Stores Amount'})
  fig.update_traces(textposition='inside', textinfo='percent+label')
  #fig.show()


  """fig = px.bar(
    x=[item.country for item in data],
    y=[item.amountStores for item in data],
    text_auto='.2s',
    title=chartTitle,
    labels={'x':xlabel, 'y': ylabel}
  )"""
  #fig.update_traces(textfont_size=27, textangle=0, textposition="outside", cliponaxis=False)
  fig.update_layout(paper_bgcolor='rgba(0, 0, 0, 0)')

  chart = fig.to_html()
  return chart

def getMean(data):
  dataAsArray = []
  for i in data:
    dataAsArray.append(i.totalStores)
  amount = np.array(dataAsArray)
  mean = "{:.2f}".format(np.mean(amount))
  return mean

#-90 and 90 latitude x
#-180 and 180 longitude y
def createDatasetLocations(latRangeMax, latRangeMin, lonRangeMax,lonRangeMin,  samplesNumber, clusterStd):
   xCoordinatesSamples, yCoordinatesLabels = make_blobs(n_samples=samplesNumber, cluster_std=clusterStd,shuffle=True, random_state=0, center_box=[[latRangeMin, lonRangeMin], [latRangeMax, lonRangeMax]])
   #displayMap(xCoordinatesSamples[:,:])
   return xCoordinatesSamples[:,:]


def displayMap(dataset):
  color_scale = [(0, 'orange'), (1,'red')]

  fig = px.scatter_mapbox(dataset, 
                        lat=dataset[:,0], 
                        lon=dataset[:,1], 
                        color_continuous_scale=color_scale,
                        zoom=2, 
                        height=500,
                        width=500)

  fig.update_layout(mapbox_style="open-street-map")
  fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
  #fig.show()
  map = fig.to_html()
  return map

from random import randint
from django.db import models
from msilib.schema import Class
import pandas as pd

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


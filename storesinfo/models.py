from django.db import models
from msilib.schema import Class

# Create your models here.
class Store(models.Model):
  store_code = models.CharField(max_length=12)
  store_class = models.CharField(max_length=12)
  name = models.CharField(max_length=12)
  phone = models.BigIntegerField()
  city = models.CharField(max_length=15)
  country = models.CharField(max_length=15)
  country_code = models.CharField(max_length=15)
  longitude = models.FloatField(max_length=12)
  latitude = models.FloatField(max_length=12)
  mon_open_hours = models.CharField(max_length=15)
  tue_open_hours = models.CharField(max_length=15)
  wed_open_hours = models.CharField(max_length=15)
  thu_open_hours = models.CharField(max_length=15)
  fri_open_hours = models.CharField(max_length=15)
  sat_open_hours = models.CharField(max_length=15)
  sun_open_hours = models.CharField(max_length=15)
  streetName1 = models.CharField(max_length=25)
  streetName2 = models.CharField(max_length=25)
  state = models.CharField(max_length=15)
  address_string = models.CharField(max_length=35)

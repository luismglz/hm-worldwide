from multiprocessing.dummy import Manager
from pickle import TRUE
from django.db import models
from msilib.schema import Class
from .shared import generateID


class StoreManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

# Create your models here.
class Store(models.Model):
  store_code = models.CharField(primary_key=True,max_length=6, default=generateID)
  store_class = models.CharField(max_length=50,null=True)
  name = models.CharField(max_length=120,null=True)
  phone = models.BigIntegerField(null=True)
  city = models.CharField(max_length=120,null=True)
  country = models.CharField(max_length=120,null=True)
  country_code = models.CharField(max_length=120,null=True)
  longitude = models.FloatField(max_length=50,null=True)
  latitude = models.FloatField(max_length=50,null=True)
  mon_open_hours = models.CharField(max_length=50,null=True)
  tue_open_hours = models.CharField(max_length=50,null=True)
  wed_open_hours = models.CharField(max_length=50,null=True)
  thu_open_hours = models.CharField(max_length=50,null=True)
  fri_open_hours = models.CharField(max_length=50,null=True)
  sat_open_hours = models.CharField(max_length=50,null=True)
  sun_open_hours = models.CharField(max_length=50,null=True)
  streetName1 = models.CharField(max_length=150,null=True)
  streetName2 = models.CharField(max_length=150,null=True)
  state = models.CharField(max_length=120, null=True)
  address_string = models.CharField(max_length=255, null=True)

  objects = models.Manager()
  #objects = models.Manager()
  #all_stores = StoreManager() # The Dahl-specific manager.
  stores_obj = StoreManager()







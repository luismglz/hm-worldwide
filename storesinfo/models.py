from multiprocessing.dummy import Manager
from pickle import TRUE
from django.db import models
from django_mysql.models import ListCharField

from django.forms import CharField, FloatField
from .shared import generateID


class StoreManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class PopulationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class KmeanManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


# Create your models here.
class Population(models.Model):
  titleSet = models.CharField(max_length=120, null=True)
  #longitudeRangeMax = models.FloatField(max_length=50,null=False)
  #longitudeRangeMin = models.FloatField(max_length=50,null=False)
  #latitudeRangeMax = models.FloatField(max_length=50,null=False)
  #latitudeRangeMin = models.FloatField(max_length=50,null=False)
  #samplesNumber = models.IntegerField(null=False)
  #clusterStd = models.FloatField(null=False)
  latitudes = models.TextField()
  longitudes = models.TextField()

  objects = models.Manager()
  populations_obj = PopulationManager()
  def getAll():
    return list(Population.objects.all())
  
  def getPopulationById(id):
    query = f"SELECT * FROM hm.storesinfo_population WHERE id={id}"
    return list(Population.objects.raw(query))


class KMeans(models.Model):
  titleCluster = models.CharField(max_length=120, null=True)
  clustersNumber = models.IntegerField(null=False)
  tolerance = models.FloatField(null=False)
  numberIterations = models.IntegerField(null=False)

  objects = models.Manager()
  kmeans_obj = KmeanManager()
  def getAll():
    return list(KMeans.objects.all())
  
  def getKmeanById(id):
    query = f"SELECT * FROM hm.storesinfo_kmeans WHERE id={id}"
    return list(KMeans.objects.raw(query))

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

  def getAll():
    return list(Store.objects.all())

  def getTopFiveMostStores():
    query = 'SELECT store_code,country, COUNT(*) AS amount FROM hm.storesinfo_store GROUP BY country ORDER BY amount DESC LIMIT 5'
    return list(Store.objects.raw(query))

  def getTopFiveFewestStores():
    query = 'SELECT store_code,country, COUNT(*) AS amount FROM hm.storesinfo_store GROUP BY country ORDER BY amount ASC LIMIT 5'
    return list(Store.objects.raw(query))

  def getCitiesMostStores():
    query = 'SELECT store_code,city , COUNT(*) AS amount FROM hm.storesinfo_store GROUP BY city ORDER BY amount DESC LIMIT 5'
    return list(Store.objects.raw(query))

  def getCitiesFewestStores():
    query = 'SELECT store_code,city, COUNT(*) AS amount FROM hm.storesinfo_store GROUP BY city ORDER BY amount ASC LIMIT 5'
    return list(Store.objects.raw(query))

  def getAmountByCountry():
    query = 'SELECT store_code,country, COUNT(country) as amountStores FROM hm.storesinfo_store GROUP BY country HAVING COUNT(country) >= 1 ORDER BY amountStores DESC'
    return list(Store.objects.raw(query))

  def getAmountByCity():
    query = 'SELECT store_code, COUNT(city)  AS totalStores FROM hm.storesinfo_store  GROUP BY city'
    return list(Store.objects.raw(query))

  def getTop5CitiesMostStores(country):
    query = f"SELECT store_code ,city , COUNT(*) AS amount FROM hm.storesinfo_store WHERE country = '{country}'GROUP BY city ORDER BY amount DESC LIMIT 5"
    return list(Store.objects.raw(query))

  def getCityMostStores():
    query = "SELECT store_code,city,COUNT(city)  AS totalStores FROM hm.storesinfo_store  GROUP BY city ORDER BY totalStores  DESC LIMIT 1"
    return list(Store.objects.raw(query))


  def getRandomCountries(amount):
    query = f"SELECT * FROM hm.storesinfo_store ORDER BY RAND () LIMIT {amount}"
    return list(Store.objects.raw(query))








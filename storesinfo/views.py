from distutils.command.sdist import sdist
from functools import singledispatchmethod
import json
from multiprocessing import context
from operator import index
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from .models import KMeans, Population, Store
from .shared import dataToDataframe, displayBarChart, getMean, displayPieChart
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import matplotlib.pyplot as plt, mpld3
import plotly.tools as tls
import plotly.express as px
import plotly.graph_objs as pgo
from plotly.graph_objs import Marker
import plotly.graph_objects as go



from storesinfo import shared


# Create your views here.
class HmView(View):
  def home(request):
    stores = Store.getAll()
    content = dataToDataframe(stores)
    return render(request, 'home.html', {"stores": content})

  def locations(request):
    return render(request, 'locations.html')

  def metrics(request):
    countries_top_most = Store.getTopFiveMostStores()
    countries_top_fewest = Store.getTopFiveFewestStores()
    cities_most_stores= Store.getCitiesMostStores()
    cities_fewest_stores= Store.getCitiesFewestStores()
    get_cities = Store.getAmountByCity()
    mean = getMean(get_cities)
    city_most_stores = Store.getCityMostStores()
    context = {
      "countriesMost":countries_top_most,
      "countriesFewest":countries_top_fewest,
      "citiesMost":cities_most_stores,
      "citiesFew":cities_fewest_stores,
      "mean":mean,
      "cityMost":city_most_stores,
    }
    return render(request, 'metrics.html',context)

  def charts(request):
    dataAmountByCountry = Store.getAmountByCountry()
    barChartAmountByCountry = displayBarChart(dataAmountByCountry,'Stores by country', 'Stores amount', 'Country')

    dataTop5CitiesMostStoresJP = Store.getTop5CitiesMostStores(country='Japan')
    pieChartTop5CitiesJP = displayPieChart(dataTop5CitiesMostStoresJP, 'Japan')

    dataTop5CitiesMostStoresMX = Store.getTop5CitiesMostStores(country='Mexico')
    pieChartTop5CitiesMX = displayPieChart(dataTop5CitiesMostStoresMX, 'Mexico')
    
    context = {
      'barAmountByCountry': barChartAmountByCountry,
      'pieTopJP': pieChartTop5CitiesJP,
      'pieTopMX': pieChartTop5CitiesMX,
    }
    return render(request, 'charts.html', context)


   # def getRandomLocations(request):
      

      #random = [randrange(4200),randrange(4200),randrange(4200),randrange(4200)]

  @csrf_exempt
  def populations(request):
    populations = Population.getAll()
    """population = Population.getPopulationById(1)
    populationsJson = []
    lats = np.array(shared.parseStrToJson(populations[0].latitudes))
    data = []

    for i in range(len(populations)):
      populationsJson.append([shared.parseStrToJson(populations[i].latitudes),shared.parseStrToJson(populations[i].longitudes)])
      for k in range(len(populationsJson[i][0])):
        data.append([populationsJson[i][0][k], populationsJson[i][1][k]])
    
    allLocations = np.array(data)"""
    
    context = {
      "populations":populations
    }
    return render(request, 'populations.html', context)


#-90 and 90 latitude x
#-180 and 180 longitude y
  def addPopulation(request):

    if request.method == "POST":
      titleSet = request.POST['titleSet']
      longitudeRangeMax = float(request.POST['longitudeRangeMax'])
      longitudeRangeMin = float(request.POST['longitudeRangeMin'])
      latitudeRangeMax = float(request.POST['latitudeRangeMax'])
      latitudeRangeMin = float(request.POST['latitudeRangeMin'])
      samplesNumber = int(request.POST['samplesNumber'])
      clusterStd = float(request.POST['dispersion'])


      data = shared.createDatasetLocations(
        latRangeMax=latitudeRangeMax,
        latRangeMin=latitudeRangeMin,
        lonRangeMax=longitudeRangeMax,
        lonRangeMin=longitudeRangeMin,
        samplesNumber=samplesNumber,
        clusterStd=clusterStd
        )
      """population = Population(
        titleSet = titleSet,
        longitudeRangeMax = longitudeRangeMax,
        longitudeRangeMin = longitudeRangeMin,
        latitudeRangeMax = latitudeRangeMax,
        latitudeRangeMin = latitudeRangeMin,
        samplesNumber = samplesNumber,
        clusterStd = clusterStd,
      )"""
      population = Population(
        titleSet = titleSet,
        latitudes = data[0],
        longitudes = data[1]
      )
      
      population.save()
      return redirect('populations')
      #return HttpResponse(population.latitudeRange)

  def addKmean(request):

    populations = Population.getAll()
    k_means = KMeans.getAll()
    print(k_means)

    if request.method == "POST":
      title = request.POST['title']
      tolerance = float(request.POST['tolerance'])
      numIterations = int(request.POST['numIterations'])
      clustersNum = int(len(populations))

      allLocations = shared.getAllCoordinates(populations)[0]
      labels = shared.getAllCoordinates(populations)[1]
      kmeansParams = shared.trainKMeans(clustersNum, numIterations,tolerance, allLocations)
      print(labels)

      kmeanSettings = KMeans(
        titleCluster= title,
        clustersNumber= clustersNum,
        tolerance= tolerance,
        numberIterations = numIterations
      )
      
      kmeanSettings.save()
      
      print(kmeansParams[0])
      map = shared.clusterLocationsMap(
        allLocations, 
        kmeansParams[0], 
        clustersNum, 
        title)
      
     

      #fig.show()

      
      
      context = {
      #'km': plt,
      "clusterMap": map,
      "k_means": k_means
      }
      return render(request, 'kmeans.html', context)
      #return redirect('kmeans')





  def createPopulationMap(request):
    if request.method == "POST":
      id = request.POST['cluster']
      clusterArgs = Population.getPopulationById(id)
      
      #parse string of json to json with locations data from mysql
      latitudes = shared.parseStrToJson(clusterArgs[0].latitudes)
      longitudes = shared.parseStrToJson(clusterArgs[0].longitudes)

      #create a tuple with lat and lon
      locations = np.array([latitudes,longitudes])

      #create map send locations tuple
      map = shared.displayMap(locations[:,:])

      #get populations to fill select options
      populations = Population.getAll()
      

      context = {
      'map': map,
      "populations":populations
      }
      
     
      return render(request, 'populations.html', context)
      #return HttpResponse(population.latitudeRange)

  def getPopulationById(request, id):
    #if request.method == "POST":
    #id = int(request.POST['id'])
    population = Population.objects.get(pk=id)
    data = []
    #locations = np.array([la])
    # population = Population.getPopulationById(int(id))

    #parse string of json to json with locations data from mysql
    lat = shared.parseStrToJson(population.latitudes)
    lng = shared.parseStrToJson(population.longitudes)

    data.append({
      "title" : population.titleSet, 
      "lat" : lat, 
      "lng" : lng})
# data = serializers.serialize('json', rawData)
    return JsonResponse(data, safe=False)



  def kmeans(request):
    populations = Population.getAll()
    k_means = KMeans.getAll()
    print(k_means)
    context = {
      "k_means":k_means
      }
   # print(Store.getRandomCountries(20))
    return render(request, 'kmeans.html', context)

  def displayKmean(request):

    populations = Population.getAll()
    k_means = KMeans.getAll()
    print(k_means)

    if request.method == "POST":
      id = int(request.POST['id'])
      k_mean = KMeans.getKmeanById(id)
      clustersNum = int(len(populations))
      allLocations = shared.getAllCoordinates(populations)[0]
      labels = shared.getAllCoordinates(populations)[1]
      kmeansParams = shared.trainKMeans(clustersNum, k_mean[0].numberIterations,k_mean[0].tolerance, allLocations)
      map = shared.clusterLocationsMap(
        allLocations, 
        kmeansParams, 
        clustersNum, 
        labels,
        k_mean[0].titleCluster)

      context = {
        "k_means":k_means,
        "clusterMap": map,
      } 
      return render(request, 'kmeans.html', context)



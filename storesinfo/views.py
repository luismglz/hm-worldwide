from distutils.command.sdist import sdist
from functools import singledispatchmethod
import json
from multiprocessing import context
from operator import index
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from .models import Population, Store
from .shared import dataToDataframe, displayBarChart, getMean, displayPieChart
from django.views.decorators.csrf import csrf_exempt
import numpy as np


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

  def createPopulationMap(request):
    if request.method == "POST":
      id = request.POST['cluster']
      clusterArgs = Population.getPopulationById(id)
      
      #parse string of json to json with locations data from mysql
      latitudes = json.loads(clusterArgs[0].latitudes)
      longitudes = json.loads(clusterArgs[0].longitudes)

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


  def clusters(request):
   # print(Store.getRandomCountries(20))
    return render(request, 'clusters.html')


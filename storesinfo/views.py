from distutils.command.sdist import sdist
from functools import singledispatchmethod
from multiprocessing import context
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from .models import Store
from .shared import dataToDataframe, displayBarChart, getMean, displayPieChart


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
    city_most_stores= Store.getCityMostStores()
    city_fewest_stores= Store.getCityFewestStores()
    get_cities = Store.getAmountByCity()
    mean = getMean(get_cities)

    context = {
      "countriesMost":countries_top_most,
      "countriesFewest":countries_top_fewest,
      "cityMost":city_most_stores,
      "cityFew":city_fewest_stores,
      "mean":mean
    }
    return render(request, 'metrics.html',context)

  def charts(request):
    dataAmountByCountry = Store.getAmountByCountry()
    barChartAmountByCountry = displayBarChart(dataAmountByCountry,'Stores by country', 'Stores amount', 'Country')

    dataTop5CitiesMostStoresJP = Store.getTop5CitiesMostStores(country='Japan')
    pieChartTop5CitiesJP = displayPieChart(dataTop5CitiesMostStoresJP)

    dataTop5CitiesMostStoresMX = Store.getTop5CitiesMostStores(country='Mexico')
    pieChartTop5CitiesMX = displayPieChart(dataTop5CitiesMostStoresMX)
    
    

    
    context = {
      'barAmountByCountry': barChartAmountByCountry,
      'pieTopJP': pieChartTop5CitiesJP,
      'pieTopMX': pieChartTop5CitiesMX,
    }

    return render(request, 'charts.html', context)

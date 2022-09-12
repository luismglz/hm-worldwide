from distutils.command.sdist import sdist
from functools import singledispatchmethod
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from .models import Store
from .shared import dataToDataframe, displayBarChart


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

    dict_data = {
      "countriesMost":countries_top_most,
      "countriesFewest":countries_top_fewest,
      "cityMost":city_most_stores,
      "cityFew":city_fewest_stores,
    }

    #content = dataToDataframe(stores)
    return render(request, 'metrics.html',dict_data)

  def charts(request):
    data = Store.getAmountByCountry()
    context = displayBarChart(data,'Stores by country', 'Stores amount', 'Country')
    return render(request, 'charts.html', context)

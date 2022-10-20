from distutils.command.sdist import sdist
from functools import singledispatchmethod
from multiprocessing import context
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from .models import Population, Store
from .shared import dataToDataframe, displayBarChart, getMean, displayPieChart
from django.views.decorators.csrf import csrf_exempt


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
   # print(Store.getRandomCountries(20))
    return render(request, 'populations.html')


#-90 and 90 latitude x
#-180 and 180 longitude y
  def addPopulation(request):
    if request.method == "POST":
      titleSet = request.POST['titleSet']
      longitudeRange = request.POST['longitudeRange']
      latitudeRange = request.POST['latitudeRange']
      samplesNumber = request.POST['samplesNumber']
      clusterStd = request.POST['dispersion']
      population = Population(
        titleSet = titleSet,
        longitudeRange = longitudeRange,
        latitudeRange = latitudeRange,
        samplesNumber = samplesNumber,
        clusterStd = clusterStd,
      )
      population.save()
     # print(population.titleSet)
      return redirect('populations')
      #return HttpResponse(population.latitudeRange)


  def clusters(request):
   # print(Store.getRandomCountries(20))
    return render(request, 'clusters.html')


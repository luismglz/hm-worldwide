from distutils.command.sdist import sdist
from functools import singledispatchmethod
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from .models import Store
from .shared import dataToDataframe


# Create your views here.
class HmView(View):
  def home(request):
    stores = Store.getAll()
    content = dataToDataframe(stores)
    return render(request, 'home.html', {"stores": content})

  def locations(request):
    return render(request, 'locations.html')

  def metrics(request):
    return render(request, 'metrics.html')

  def charts(request):
    return render(request, 'charts.html')

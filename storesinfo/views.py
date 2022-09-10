from distutils.command.sdist import sdist
from functools import singledispatchmethod
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from .models import Store

# Create your views here.
class HmView(View):
  def home(request):
    #stores = AllSoresManager.get_queryset(self)
    #stores = Store.all_stores.all()
    stores = list(Store.objects.all())
    print(type(stores))
    print(len(stores))
    print(stores[200].name)
    
   # if len(stores)>0:
   #   data = {'message': 'success'}
    #return JsonResponse(data)
    return HttpResponse(request,stores)
    #return render(request, 'home.html', {"stores": stores})

  def locations(request):
    return render(request, 'locations.html')

  def metrics(request):
    return render(request, 'metrics.html')

  def charts(request):
    return render(request, 'charts.html')

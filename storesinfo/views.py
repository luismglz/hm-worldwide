from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
def home(request):
  return render(request, 'home.html')

def locations(request):
  return render(request, 'locations.html')

def metrics(request):
  return render(request, 'metrics.html')

def charts(request):
  return render(request, 'charts.html')
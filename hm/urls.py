"""hm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pathlib import Path
from django.contrib import admin
from django.urls import path
from storesinfo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HmView.home, name="home"),
    path('locations/', views.HmView.locations, name="locations"),
    path('metrics/', views.HmView.metrics, name="metrics"),
    path('charts/', views.HmView.charts, name="charts"),
    path('populations/', views.HmView.populations, name="populations"),
    path('populations/add/', views.HmView.addPopulation, name="addPopulations"),
    path('clusters/', views.HmView.clusters, name="clusters"),
]

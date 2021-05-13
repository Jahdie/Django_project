"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from dict.views import *

urlpatterns = [
    path('', index),
    path('upload/', upload),
    path('dict/<int:dict_number>/', getListDictionary),
    path('dict/<int:dict_number>/<int:dict_number_number>/', getListRelatedDictionary)
    # path('dict/dicts.html', getListDictionaryControllerFamilies),
    # path('dict/dicts.html', getListDictionaryLocations),

]

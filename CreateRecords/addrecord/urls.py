from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views
from django.http import HttpResponse

urlpatterns = [
               
               url(r'^$', views.index, name = "index"), 
               
               ]
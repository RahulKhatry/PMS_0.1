from django.shortcuts import render
from django.http import HttpResponse
from urllib2 import urlopen
from json import *
# Create your views here.



def index(request):
    return HttpResponse('Good')




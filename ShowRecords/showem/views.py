from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import *
from django.conf import settings
import requests
from bson.json_util import dumps
from pymongo import *
from .form import SearchForm
from json import loads
import json


def index(request):

    form  = SearchForm(data = request.POST)
    s1 = 1
    IDs = {
           "form" : form 
           }

    if form.is_valid():
        Client  = MongoClient('Rahul-PC', 27017)
        db = Client.test
        coll = db.test
        s1 = form.cleaned_data.get("SearchAN")
        cursor1 = coll.find_one({"Appointment_Number":"%s"%(s1)})
#         x1 = dumps(cursor1)
#         x = loads(x1)
        x= cursor1
        IDs = {
           "form" : form,
           "Name" : x['name'], 
           "Appointment_Date" : x['Appointment_Date'], 
           "Appointment_Time" : x['Appointment_Time'], 
           "email_ID" : x['emailID'], 
            "Phone_Number" : x['Phone'] 
           }
        return render(request, 'appointment.html',IDs)
        
    
    return render(request, 'appointment.html',IDs)


# def index2(request):
#     Client  = MongoClient('Rahul-PC', 27017)
#     db = Client.test
#     coll = db.test
#     data = {"name":"Ronda","surname":"Wanda","booter":"@olton"}
#     coll.insert(data)
#     return HttpResponse('yo')
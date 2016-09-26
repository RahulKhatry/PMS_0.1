from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import *
from django.conf import settings
import requests
import json

from mongoengine import connect
from mongoengine import *
from mongoengine.context_managers import switch_db 
from pymongo import *
from .form import AppointmentForm

from django.core.mail import send_mail
import crispy_forms
import smtplib






def index(request):

    if request.user.is_authenticated():
        
        app_number = 1
        address_open = "http://127.0.0.1:8080/Employees/api/%s/?format=json"%(app_number)
        r = requests.get(address_open)
        edata = r.json()
        form = AppointmentForm(request.POST or None)
        IDs = {'ID':edata['id'],
           'Name':edata['EName'],
           'HD':edata['HiringDate'],
           'eid':edata['emailID'],
           "form": form
           }
        
        if form.is_valid():
           instance = form.save(commit = False)     
           N2 = instance.Name
           EID2 = instance.emailID
           AD = instance.Appointment_Date
           AT = instance.Appointment_Time
           AN = instance.Appointment_Number
           DE = "rahulkhatry4@gmail.com"
           PH = instance.Phone
           data = {"name":"%s"%(N2),"Appointment_Date":"%s"%(AD),"Appointment_Time":"%s"%(AT),"emailID":"%s"%(EID2),"Appointment_Number":"%s"%(AN), "Phone":"%s"%(PH)}
           
           Client  = MongoClient('Rahul-PC', 27017)
           db = Client.test
           coll = db.test
           coll.insert(data)
           Client.close()
           
           s=smtplib.SMTP("smtp.gmail.com:587")
           s.ehlo()
           s.starttls()
           s.login("rahulkhatry23@gmail.com", "bialamos")
           
           SUBJECT = "Appointment Booked"
           TEXT = "Hi %s Your Appointment Booked for %s at %s"%(N2, AD, AT)
           To = "%s"%(EID2)
           
           message = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
           
           s.sendmail('rahulkhatry23@gmail.com',To , message)
#            send_mail('Appointment Booked', 'Your Appointment has been booked for at' , 'rahulkhatry23@gmail.com', [DE ,EID2], fail_silently=False)
           IDs = {
            'Name':"Thank You!",
            }
           
        return render(request, 'appointment.html',IDs)
    

    return render(request, 'appointment.html')

# def index2(request):
#     Client  = MongoClient('Rahul-PC', 27017)
#     db = Client.test
#     coll = db.test
#     data = {"name":"Ronda","surname":"Wanda","booter":"@olton"}
#     coll.insert(data)
#     return HttpResponse('yo')
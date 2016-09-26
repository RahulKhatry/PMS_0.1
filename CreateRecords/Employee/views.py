from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from models import EmployeeRecords
from serializers import EmployeeSerializer

# list all employees or create a new one
class EmployeeList(generics.ListCreateAPIView):

        queryset = EmployeeRecords.objects.all()
        serializer_class = EmployeeSerializer
    
    
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeRecords.objects.all()
    serializer_class = EmployeeSerializer
    

from django.db import models

# Create your models here.

class Appointment(models.Model):
    Name = models.CharField(max_length = 50)
    Appointment_Number = models.IntegerField()
    Appointment_Date = models.DateField(help_text = 'dd/mm/yy')
    Appointment_Time = models.TimeField(help_text = 'hh:mm:ss')
    Phone = models.IntegerField()
    emailID = models.CharField(max_length = 60)
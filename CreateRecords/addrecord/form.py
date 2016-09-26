from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        Appointment_Date = forms.DateField(widget=SelectDateWidget())
        
        fields = '__all__'

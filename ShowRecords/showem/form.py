from django import forms
from django.forms.extras.widgets import SelectDateWidget


class SearchForm(forms.Form):
        SearchAN = forms.IntegerField()
        
        fields = '__all__'



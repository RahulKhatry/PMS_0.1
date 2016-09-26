from django.db import models

# Create your models here.

class EmployeeRecords(models.Model):
    EName = models.CharField(max_length=60)
    HiringDate = models.DateField(help_text = 'date published')
    emailID = models.CharField(max_length = 60)
    upload = models.FileField(upload_to='photos/')
    
    def __str__(self):
        return self.EName
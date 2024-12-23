from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.utils.timezone import now 

# Create your models here.

class City(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city_name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)   
    date=models.DateField(default=now, blank=True)
    notes= models.TextField()
    lng=models.FloatField(default=0.0)
    lat=models.FloatField(default=0.0)

def __str__(self):
    return f'{self.city_name} ,{self.country}'

 
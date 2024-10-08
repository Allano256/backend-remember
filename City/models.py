from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    city_name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    emoji= models.CharField(max_length=5)   
    date=models.DateField(auto_now_add=True)
    notes= models.TextField()
    lat=models.FloatField()
    lng=models.FloatField()


def __str__(self):
    return f'{self.city_name} ,{self.country}'

 
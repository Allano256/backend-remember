from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    city_name=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    notes= models.TextField();

def __str__(self):
    return f'{self.cty_name} {self.date} {self.notes}'

 
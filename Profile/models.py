
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class Profile(models.Model):

    user= models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=100, default='')
    email=models.EmailField(max_length=250,  default='')
    password=models.CharField(max_length=50, default='')
    image=models.ImageField(
        upload_to='images/', default='../default_profile_kstxax'
    )
   
   

    def __str__(self):
        return f"{self.user} 's profile"
    
    #This will create Profile when new user signs up
    def create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile=Profile.objects.create(user=instance)
            user_profile.save()

    post_save.connect(create_profile, sender=User)

class Note(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    city_name=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    notes= models.TextField();

 

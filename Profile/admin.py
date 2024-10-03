from django.contrib import admin
from .models import Profile, Note
from django.contrib.auth.models import Group,User

# Register your models here.

#Unregister Groups
admin.site.unregister(Group)

#Mix profile info into User info
class ProfileInline(admin.StackedInline):
    model = Profile

#Extend User Model
class userAdmin(admin.ModelAdmin):
    model=User
    fields=['username']
    inlines=[ProfileInline]

#Unregister initial user
admin.site.unregister(User)
#Reregister user
admin.site.register(User,userAdmin)


# admin.site.register(Profile)
admin.site.register(Note)


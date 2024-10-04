from django.urls import path
from . import views

urlpatterns = [
    path('activity/',views.ActivityList.as_view()),
]

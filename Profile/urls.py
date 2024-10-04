from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ProfileCreate.as_view(), name='create-profile'),
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
]



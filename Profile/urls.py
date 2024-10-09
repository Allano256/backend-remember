from django.urls import path
from . import views
from .views import CustomLoginView


urlpatterns = [
  
   
    path('register/', views.user_registration_view, name='register'),
    path('dj-rest-auth/login', CustomLoginView.as_view(),name='login' ),
    path('logout/', views.user_logout, name='logout'),
]



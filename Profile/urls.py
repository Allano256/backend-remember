from django.urls import path
from . import views


urlpatterns = [
  
    # path('create/', views.ProfileCreate.as_view(), name='create-profile'),
    # path('profiles/', views.ProfileList.as_view()),
    # path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('register/', views.user_registration_view, name='register'),
    path('logout/', views.user_logout, name='logout'),
]



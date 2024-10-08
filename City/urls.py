from django.urls import path
from . import views

urlpatterns = [
    path('cities/',views.CityListCreateView.as_view(), name='cities'),
    path('cities/<int:pk>/',views.CityDetailView.as_view(), name='cities'),
]

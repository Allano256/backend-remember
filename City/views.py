from django.shortcuts import render
from .models import City
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Cityserializer
from django.http import Http404
from drf_api.permissions import IsOwnerOrReadOnly

from rest_framework import generics
from .models import City
from .serializers import Cityserializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication



class CityListCreateView(generics.ListCreateAPIView):
    queryset=City.objects.all()
    serializer_class=Cityserializer
    permission_classes=[IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    


class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=City.objects.all()
    serializer_class=Cityserializer
    permission_classes= [IsAuthenticated]





# # Create your views here.
# class CityList(APIView):
#     serializer_class= Cityserializer
#     permission_classes=[permissions.IsAuthenticated]

#     def get(self, request):
#         city=City.objects.all()
#         serializer= Cityserializer(
#             city, many=True, context={'request': request}
#         )
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer=Cityserializer(
#             data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )
    
# class CityDetail(APIView):
#     permission_classes= [IsOwnerOrReadOnly]
#     serializer_class= Cityserializer

#     def get_object(self,request, pk):
#         try:
#             city=City.objects.get(pk=pk)
#             self.check_object_permissions(self.request, city)
#             return city
#         except City.DoesNotExist:
#             raise Http404
       
        
#     def get(self, request, pk):
#         city= self.get_object(pk)
#         serializer= Cityserializer(
#             city, context={'request': request}
#         )
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         city = self.get_object(pk)
#         serializer = Cityserializer(
#             city, data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )
    
#     def delete(self, request, pk):
#         city= self.get_object(pk)
#         city.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )
    
        

  
   
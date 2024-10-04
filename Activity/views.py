from django.shortcuts import render
from .models import Activity
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Activityserializer
from django.http import Http404
from drf_api.permissions import IsOwnerOrReadOnly

# Create your views here.

class ActivityList(APIView):
    serializer_class= Activityserializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        activities=Activity.objects.all()
        serializer= Activityserializer(
            activities, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer=Activityserializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    
class ActivityDetail(APIView):
    permission_classes= [IsOwnerOrReadOnly]
    serializer_class= Activityserializer

    def get_object(self, pk):
        try:
            activity=Activity.objects.get(pk=pk)
            self.check_object_permissions(self.request, activity)
            return activity
        except Activity.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        activity= self.get_object(pk)
        serializer= Activityserializer(
            activity, context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        activity = self.get_object(pk)
        serializer = Activityserializer(
            activity, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        activity= self.get_object(pk)
        activity.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
    
        

  
   
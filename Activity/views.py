from django.shortcuts import render
from .models import Activity
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Activityserializer

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
  
   
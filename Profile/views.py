from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, User
from .serializers import ProfileSerializer
from django.http import Http404
from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view


class ProfileList(APIView):
    def get(self,request):
        profiles=Profile.objects.all()
        serializer= ProfileSerializer(profiles, many=True, context={'request': request})
        return Response(serializer.data)


class ProfileDetail(APIView):
    serializer_class=ProfileSerializer
    permission_classes=[IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            profile= Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        profile=self.get_object(pk)
        serializer= ProfileSerializer(profile,  context={'request': request})
        return Response(serializer.data)
    
    def put(self,request,pk):
        profile=self.get_object(pk)
        serializer=ProfileSerializer(profile, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileCreate(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
     
        user_data = {
            'username': request.data.get('username'),
            'email': request.data.get('email'),
            'password': request.data.get('password')
        }
        
        # Create user
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )
        
        # Now create the profile and link it to the user
        profile_data = request.data
        profile_data['user'] = user.id 

        serializer = ProfileSerializer(data=profile_data)
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Assign the user to the profile's owner field
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
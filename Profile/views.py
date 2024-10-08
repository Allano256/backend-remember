from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  User
from .serializers import ProfileSerializer, CustomLoginSerializer
from django.http import Http404
from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import  Token


from dj_rest_auth.views import LoginView


class CustomLoginView(LoginView):
    serializer_class= CustomLoginSerializer




@api_view(['POST'])
def user_registration_view(request):
    if request.method=='POST':
        serializer=ProfileSerializer(data= request.data)


        data= {}

        if serializer.is_valid():
            account= serializer.save()


            data['response']= 'Account has been created'
            data['username']= account.username
            data['email']= account.email

            token=Token.objects.get(user=account).key
            data['token']=token

        else:
            data=serializer.errors
        return Response(data)
    
@api_view(['POST'])
def user_logout(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response({'Message': 'You are loggeedout'}, status=status.HTTP_200_OK)

    






# class ProfileList(APIView):
#     def get(self,request):
#         profiles=Profile.objects.all()
#         serializer= ProfileSerializer(profiles, many=True, context={'request': request})
#         return Response(serializer.data)


# class ProfileDetail(APIView):
#     serializer_class=ProfileSerializer
#     permission_classes=[IsOwnerOrReadOnly]
#     def get_object(self, pk):
#         try:
#             profile= Profile.objects.get(pk=pk)
#             self.check_object_permissions(self.request, profile)
#             return profile
#         except Profile.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         profile=self.get_object(pk)
#         serializer= ProfileSerializer(profile,  context={'request': request})
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         profile=self.get_object(pk)
#         serializer=ProfileSerializer(profile, data=request.data,  context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class ProfileCreate(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
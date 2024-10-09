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
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


class CustomLoginView(LoginView):
    serializer_class= CustomLoginSerializer
    permission_classes=[IsOwnerOrReadOnly]


@api_view(['POST'])
@permission_classes([AllowAny])
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

    






from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    username = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField()
    

    class Meta(UserDetailsSerializer.Meta):
          fields = ('pk', 'username', 'password', 'first_name' ) 
        
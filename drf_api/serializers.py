from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='username')
    

    class Meta(UserDetailsSerializer.Meta):
         fields = UserDetailsSerializer.Meta.fields + ('username',)
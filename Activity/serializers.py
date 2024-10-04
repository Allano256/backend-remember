from rest_framework import serializers
from .models import Activity


class Activityserializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.usernameusername')
    is_owner= serializers.SerializerMethodField()
   

    def get_is_owner(self, obj):
        request=self.context['request']
        return request.user == obj.user


    class Meta:
        model= Activity
        fields =[
            'city_name','date','notes','is_owner','owner'
        ]



from rest_framework import serializers
from .models import City


class Cityserializer(serializers.ModelSerializer):
  
   

    def get_is_owner(self, obj):
        request=self.context['request']
        return request.user == obj.user


    class Meta:
        model= City
        fields =[
            'id','city_name','country', 'date','notes','lat','lng'
        ]



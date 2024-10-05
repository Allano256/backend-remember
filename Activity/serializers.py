from rest_framework import serializers
from .models import Activity


class Activityserializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    is_user= serializers.SerializerMethodField()
   

    def get_is_owner(self, obj):
        request=self.context['request']
        return request.user == obj.user


    class Meta:
        model= Activity
        fields =[
            'city_name','date','notes','is_user','user'
        ]



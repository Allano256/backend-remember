from rest_framework import serializers

from django.contrib.auth.models import User
from dj_rest_auth.serializers import LoginSerializer


class ProfileSerializer(serializers.ModelSerializer):
    # password2 =serializers.CharField(style={'input_type': 'password'}, write_only=True)
   
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model=User
        fields =['username', 'email', 'password', 'password2', ]
        extra_kwargs={
            'password': {'write_only':True}
        }


        def validate(self, data):
            if data['password'] != data['password2']:
                raise serializers.ValidationError(_("Passwords do not match."))
            return data

    def create(self, validated_data):
       
        validated_data.pop('password2')
        
        # Create the user
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
           
           
        )
        user.set_password(validated_data['password'])  
        user.save()  
        return user
    

class CustomLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        username=attrs.get('username')
        password= attrs.get('password')

        if not username and not password:
            raise serializers.ValidationError('Please provide valid username and password')
        
        return super().validate(attrs)























# class ProfileSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.username')

#     is_user =serializers.SerializerMethodField()

#     def get_is_owner(self, obj):
#         request = self.context['request']
#         return request.user == obj.user

#     class Meta:
#         model= Profile
#         fields =[
#             'id', 'user', 'username','email','password','image', 'is_user', 
#         ]

#     def create(self, validated_data):
#         # validated_data.pop('confirm_password') 
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         profile = Profile.objects.create(user=user, **validated_data)
#         return profile

#     def validate_username(self, value):
#         if User.objects.filter(username=value).exists():
#             raise serializers.ValidationError('The username is already taken')
#         return value
    
  
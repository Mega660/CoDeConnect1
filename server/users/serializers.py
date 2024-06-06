from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    ''' Serializer for the User model '''

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        ''' Create and return a new user '''

        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


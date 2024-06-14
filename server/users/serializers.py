from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

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


class LoginSerializer(serializers.Serializer):
    ''' Serializer for the login view '''

    email = serializers.CharField()
    id = serializers.CharField(max_length=15, read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        ''' Validate the data '''

        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError('An email is required to log in')
        if password is None:
            raise serializers.ValidationError('A password is required to log in')
        
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError('A user with that email and password was not found')
        
        return {
            "email": user.email,
            "id": user.id
        }

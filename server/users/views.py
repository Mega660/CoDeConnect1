from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .tokenauthentication import JWTAuthentication
from .serializers import UserSerializer, LoginSerializer

@api_view(['POST'])
def register_user(request):
    ''' Register a new user '''
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    ''' Log in a user '''
    
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        token = JWTAuthentication.generate_token(payload=serializer.validated_data)
        return Response({
            "message": 'Login successful',
            "token": token,
            "user": serializer.data
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

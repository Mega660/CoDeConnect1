import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

User = get_user_model()

class JWTAuthentication(BaseAuthentication):
    ''' Custom JWT authentication class '''

    def authenticate(self, request):
        ''' Authenticate the user '''
        
        token = self.extract_token(request=request)
        if token is None:
            return None
        
        try:
            payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=['HS256'])
            self.verify_token(payload=payload)

            user_id = payload["id"]
            user = User.objects.get(id=user_id)
            return user
        except (InvalidTokenError, ExpiredSignatureError, User.DoesNotExist):
            raise AuthenticationFailed('Invalid token')


    def verify_token(self, payload):
        ''' Verify the token '''

        if "exp" not in payload:
            raise InvalidTokenError('Token is missing the expiration date')

        exp_timestamp = payload['exp']
        current_timestamp = datetime.now().timestamp()
        if current_timestamp > exp_timestamp:
            raise ExpiredSignatureError('Token has expired')


    def extract_token(self, request):
        ''' Extract the token from the request '''
        
        auth_header = request.headers.get('Authorization', None)
        if auth_header and auth_header.startswith('Bearer '):
            return auth_header.split(' ')[1]
        return None


    @staticmethod
    def generate_token(payload):
        ''' Generate a new token '''
        
        expiration = datetime.now() + timedelta(days=1)
        payload['exp'] = expiration
        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256')
        return token

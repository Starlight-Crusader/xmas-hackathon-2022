from django.contrib.auth import hashers
from rest_framework import generics, status, response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from authen import serializers
from users import models
import datetime
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


# AUTHENTICATION

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = models.User.objects.get(email=serializer.data['email'])
        if user.check_password(serializer.data['password']) is False:
            return response.Response('Password is incorrect.',
                                     status=status.HTTP_400_BAD_REQUEST)
    except models.User.DoesNotExist:
        return response.Response('User does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)
    try:
        token = Token.objects.get(user=user)
    except Token.DoesNotExist:
        token = Token.objects.create(user=user)

    user.last_login = datetime.datetime.now()
    data = {
        "id": user.id,
        "email": user.email,
        "is_staff": user.is_staff,
        "auth_token": token.key
    }

    return response.Response(data)


# PASSWORD CHANGE

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = serializers.ChangePasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = models.User.objects.get(user = request.user.id)
    except models.User.DoesNotExist:
        return response.Response('User does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)

    if user.check_password(serializer.data['old_password']) is False:
        return response.Response('Old password is incorrect.',
                                 status=status.HTTP_400_BAD_REQUEST)

    if serializer.data['new_password'] != serializer.data['confirm_new_password']:
        return response.Response('Passwords do not coincide.',
                                 status=status.HTTP_400_BAD_REQUEST)

    user.password = hashers.make_password(serializer.data['new_password'])
    user.save(update_fields=['password'])

    return response.Response('The password has been updated.')


# REGISTRATION

class RegisterUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    serializer_class = serializers.RegisterUserSerializer

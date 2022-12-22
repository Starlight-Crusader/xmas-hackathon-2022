from rest_framework import generics
from users import models, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


class UserList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

from pyexpat import model
from rest_framework import serializers
from users import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = '__all__'
        extra_kwargs = {"password": {"write_only": True}, "email": {"write_only": True}}

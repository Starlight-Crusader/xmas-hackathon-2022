from pyexpat import model
from rest_framework import serializers
from helpapp import models


class CommandSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Command
        fields = '__all__'
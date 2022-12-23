from pyexpat import model
from rest_framework import serializers
from memeapp import models


class MemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Meme
        fields = '__all__'

from pyexpat import model
from rest_framework import serializers
from students import models


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = '__all__'
        
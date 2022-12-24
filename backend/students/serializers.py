from pyexpat import model
from rest_framework import serializers
from students import models


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = ['id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["question_text"] = instance.name

        return data

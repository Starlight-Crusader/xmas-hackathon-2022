from pyexpat import model
from rest_framework import serializers
from helpapp import models


class CommandSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Command
        fields = ['id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["question_text"] = instance.command_name

        return data
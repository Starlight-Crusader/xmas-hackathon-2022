from pyexpat import model
from rest_framework import serializers
from quizzes import models


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = '__all__'
        
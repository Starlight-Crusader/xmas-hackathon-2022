from django.shortcuts import render
from rest_framework import generics, status, response, serializers
from quizzes.serializers import QuestionSerializer
from quizzes import models
import random


class GetQuestions(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        data = models.Question.objects.all()
        random.shuffle(data)

        n = int(self.request.query_params.get('n'))

        return data[:n]


class QuestionsList(generics.ListCreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = QuestionSerializer

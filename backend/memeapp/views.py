from django.shortcuts import render
from rest_framework import generics
from memeapp import models, serializers

class GetMeme(generics.ListAPIView):
    serializer_class = serializers.MemeSerializer

    def get_queryset(self):
        t = self.request.query_params.get('topic')
        data = models.Meme.objects.filter(topic=t).order_by('?')

        return data[:1]

class MemeList(generics.ListCreateAPIView):
    queryset = models.Meme.objects.all()
    serializer_class = serializers.MemeSerializer

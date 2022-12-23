from django.shortcuts import render
from rest_framework import generics
from memeapp import models

class GetMeme(generics.ListAPIView):
    serializer_class = MemeSerializer

    def get_meme(self):
        t = self.request.query_params.get('topic')
        data = models.Meme.objects.filter(topic=t)

        return data

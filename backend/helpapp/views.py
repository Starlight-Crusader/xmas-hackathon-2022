from rest_framework import generics, status, response
from helpapp import serializers, models

class CommandsList(generics.ListCreateAPIView):
    queryset = models.Command.objects.all()
    serializer_class = serializers.CommandSerializer

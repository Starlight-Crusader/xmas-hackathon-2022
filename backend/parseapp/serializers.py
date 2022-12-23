from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    command = serializers.CharField()

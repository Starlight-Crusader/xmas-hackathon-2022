from django.shortcuts import render
from rest_framework import response
from rest_framework.decorators import api_view

@api_view(['GET'])
def greet_view(request):

    data = {
        "status": True
    }

    return response.Response(data)

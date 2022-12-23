from django.shortcuts import render
from nltk.tokenize import word_tokenize
from rest_framework import generics, status, response
from rest_framework.decorators import api_view
from parse import serializers

@api_view(['POST'])
def parse_command(request):
    serializer = serializers.RequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        command = serializer.data['command']
        tokens = word_tokenize(commans)

        if tokens[0] != 'vdov':
            return response.Response('Invalid shell command')
        if tokens[1] == 'help':
            return HttpResponse('')
        elif tokens[1] == 'quiz':
            if len(tokens) > 2:
                number_of_questions = int(tokens[2])
                return HttpResponse('')

            return HttpResponse('')
        elif tokens[1] == 'meme':
            if len(tokens) > 2:
                meme_topic = tokens[2]
            return HttpResponse('')
        else:
            return HttpResponse('Invalid second argument')
    except:
         return response.Response('Something went wrong', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

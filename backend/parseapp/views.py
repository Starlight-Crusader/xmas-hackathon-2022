from django.shortcuts import render
from nltk.tokenize import word_tokenize
from rest_framework import generics, status, response
from rest_framework.decorators import api_view
from parseapp import serializers

@api_view(['POST'])
def parse_command(request):
    serializer = serializers.RequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        command = serializer.data['command']
        tokens = word_tokenize(commans)

        if tokens[0] != 'vdov':
            return response.Response('Invalid shell command', status=status.HTTP_400_BAD_REQUEST)
        if tokens[1] == 'help':
            return response.Response('api/help', status=status.HTTP_200_OK)
        elif tokens[1] == 'quiz':
            if len(tokens) > 2:
                number_of_questions = tokens[2]
            else:
                number_of_questions = str(10)

            return response.Response('api/quizzes/n=' + number_of_questions, status=status.HTTP_200_OK)
        elif tokens[1] == 'meme':
            if len(tokens) > 2:
                meme_topic = tokens[2]
            else:
                meme_topic = 'default'

            return response.Response('api/memeapp/topic=' + meme_topic, status=status.HTTP_200_OK)
        else:
            return response.Response('Invalid argument', status=status.HTTP_400_BAD_REQUEST)
    except:
         return response.Response('Something went wrong', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

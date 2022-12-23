from django.shortcuts import render
from django.http import HttpResponse
from nltk.tokenize import word_tokenize

from rest_framework import generics, status, response
from rest_framework.decorators import api_view

@api_view(['POST'])
def parse_command(request):
    command = word_tokenize(request)

    if command[0] != 'vdov':
        return HttpResponse('Invalid shell command')
    
    if command[1] == 'help':
        return HttpResponse('')
    elif command[1] == 'quiz':
        if len(command) > 2:
            number_of_questions = int(command[2])
            return HttpResponse('')
        return HttpResponse('')
    elif command[1] == 'meme':
        if len(command) > 2:
            meme_topic = command[2]
        return HttpResponse('')
    else:
        return HttpResponse('Invalid second argument')


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello2(request):
    return HttpResponse('Hello!2')

def howAreYou2(request):
    return HttpResponse('How are you?2')

def goodbye2(request):
    return HttpResponse('Goodbye!2')
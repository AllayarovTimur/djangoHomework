from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('index')

def hello(request):
    return HttpResponse('Hello!')

def howAreYou(request):
    return HttpResponse('How are you?')

def goodbye(request):
    return HttpResponse('Goodbye!')
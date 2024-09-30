from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello1(request):
    return HttpResponse('Hello!1')

def howAreYou1(request):
    return HttpResponse('How are you?1')

def goodbye1(request):
    return HttpResponse('Goodbye!1')
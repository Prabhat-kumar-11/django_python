from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello User!")

def greet(request, username):
    return HttpResponse(f"Hello, {username}!")

def farewell(request, username):
    return HttpResponse(f"Goodbye, {username}!")

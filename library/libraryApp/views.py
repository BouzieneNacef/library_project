from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("home")

def book(request):
    return HttpResponse("book")

def about(request):
    return HttpResponse("about")
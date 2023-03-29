from django.shortcuts import render
from django.http import HttpResponse

def ahla(request):
    return render(request, 'welcome.html')

def home(request):
    return HttpResponse("this is the second page")


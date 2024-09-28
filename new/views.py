from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    msg = "<h1>Welcome to django</h1>"
    return HttpResponse(msg)

def home(request):
    return render(request,'home.html')

 

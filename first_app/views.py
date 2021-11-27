from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,"hello.html",{"name": 'Rohith'})

def brain(request):
    return HttpResponse("welcome to Django course")

def david(request):
    return HttpResponse("David")

def Greet(request,name):
    return HttpResponse(f"Hello {name.capitalize()}")


from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Django CI/CD Project Running Successfully")

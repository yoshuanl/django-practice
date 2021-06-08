from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('This is home page.')

def products(request):
    return HttpResponse('This is products page.')

def customer(request):
    return HttpResponse('This is customer page.')

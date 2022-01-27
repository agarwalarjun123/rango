from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(_request):
    return HttpResponse('<a href="/rango/about/">About</a> Rango says hey there partner!')
def about(_request):
    return HttpResponse('<a href="/rango/">Index</a> Rango says here is the about page.')
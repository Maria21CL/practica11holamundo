from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("PRACTICA 11 COMPUTACION EN LA NUBE <br> COMPUTACION - GARI CORONEL")

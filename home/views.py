from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    response = HttpResponse()
    response.writelines('<h1>writelines homepage</h1>')
    response.write('<h2>write homepage</h2>')
    return response

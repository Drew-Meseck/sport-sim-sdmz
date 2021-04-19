from django.shortcuts import render
from django.http import HttpResponse


#Test View
def index(request):
    return HttpResponse("Hello, world. You're at the simulation index")


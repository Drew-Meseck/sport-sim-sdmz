from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def games_view(request, *args, **kwargs):
    return render(request, "simulation.html", {})

def standings_view(request, *args, **kwargs):
    return render(request, "standings.html", {})

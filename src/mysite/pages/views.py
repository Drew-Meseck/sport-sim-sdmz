from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def games_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is the Simulation View",
        "my_number": 342,
        "my_list": ["Apples", "Oranges", "Kiwis"]
    }
    return render(request, "simulation.html", my_context)

def standings_view(request, *args, **kwargs):
    return render(request, "standings.html", {})

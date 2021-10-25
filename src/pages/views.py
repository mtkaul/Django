from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contacts_view(request, *args, **kwargs):
    return HttpResponse("<h1> Mera Contact</h1>")

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

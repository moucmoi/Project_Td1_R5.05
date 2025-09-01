from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request,param):
    return HttpResponse(f"<h1>Bonjour { param }</h1>")

def contact(request):
    return HttpResponse("<h1>Nous contater</h1><p>07 69 01 88 61</p>") 

def about(request):
    return HttpResponse("<h1>A propos de nous</h1><p>Je suis Noa</p>")
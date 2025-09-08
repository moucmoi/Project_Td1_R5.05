from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request,param=None):
    if param is None:
        return HttpResponse("<h1>Bonjour inconu</h1>")
    else:
        return HttpResponse("<h1>Bonjour "+param+"</h1>")

def contact(request):
    return HttpResponse("<h1>Nous contater</h1><p>07 69 01 88 61</p>") 

def about(request):
    return HttpResponse("<h1>A propos de nous</h1><p>Je suis Noa</p>")



def produits(request):
    html="<ul>"
    for objet in Produit.objects.all():
        html+=f"<li>{objet}</li>"
    html+="</ul>"
    return HttpResponse(html)

def categories(request):
    html="<ul>"
    for objet in Categorie.objects.all():
        html+=f"<li>{objet}</li>"
    html+="</ul>"
    return HttpResponse(html)

def status(request):
    html="<ul>"
    for objet in Statut.objects.all():
        html+=f"<li>{objet}</li>"
    html+="</ul>"
    return HttpResponse(html)
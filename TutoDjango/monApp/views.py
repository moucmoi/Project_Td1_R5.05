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
    return render(request, 'monApp/contact.html')

def about(request):
    return render(request, 'monApp/about.html')


def status(request):
    stats = Statut.objects.all()
    return render(request, 'monApp/list_statuts.html',{'stats': stats})

def rayon(request):
    rys = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html',{'rys': rys})

def produits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

def categories(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html',{'cats': cats})



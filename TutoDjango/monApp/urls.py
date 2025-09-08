from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("home/<param>", views.home, name="home"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    path("produits",views.produits,name="produits"),
    path("categories",views.categories,name="categorie"),
    path("status",views.status,name="status")
]
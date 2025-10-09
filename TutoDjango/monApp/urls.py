from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [

    path("", views.HomeView.as_view(), name="home"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("home/<param>/", views.HomeView.as_view()),

    path("about/", views.AboutView.as_view()),

    path("contact/", views.ContactView),

    path("produits/",views.ProduitListView.as_view(),name="lst_prdts"),
    path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),
    path("produit/<pk>/update/",views.ProduitUpdateView.as_view(), name="prdt-chng"),
    path("produit/",views.ProduitCreateView.as_view(), name="crt-prdt"),
    path("produit/<pk>/delete/",views.ProductDeleteView.as_view(), name="dlt-prdt"),

    path("categories/",views.CategorieListView.as_view(),name="lst_cats"),
    path("categorie/<pk>/" ,views.CategorieDetailView.as_view(), name="dtl_cat"),
    path("categorie/<pk>/update/",views.CategorieUpdateView.as_view(), name="cat-chng"),
    path("categorie/",views.CategorieCreateView.as_view(), name="crt-cat"),
    path("categorie/<pk>/delete/",views.CategorieDeleteView.as_view(), name="dlt-cat"),

    path("status/",views.StatusListView.as_view(),name="lst_stats"),
    path("statut/<pk>/" ,views.StatusDetailView.as_view(), name="dtl_stat"),
    path("statut/<pk>/update/",views.StatusUpdateView.as_view(), name="stat-chng"),
    path("statut/",views.StatusCreateView.as_view(), name="crt-stat"),
    path("statut/<pk>/delete/",views.StatusDeleteView.as_view(), name="dlt-stat"),

    path("rayons/",views.RayonListView.as_view(),name="lst_rys"),
    path("rayon/<pk>/" ,views.RayonDetailView.as_view(), name="dtl_ry"),
    path("rayon/<pk>/update/",views.RayonUpdateView.as_view(), name="ry-chng"),
    path("rayon/",views.RayonCreateView.as_view(), name="crt-ry"),
    path("rayon/<pk>/delete/",views.RayonDeleteView.as_view(), name="dlt-ry"),

    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),

    path('email-sent/',views.mailSend,name="email-sent"),

    path('rayon/<pk>/cntnr', views.ContenirCreateView.as_view(), name='cntnr-crt'),

    
]
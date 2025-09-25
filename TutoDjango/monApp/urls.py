from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [

    path("home/", views.HomeView.as_view(), name="home"),
    path("home/<param>/", views.HomeView.as_view()),

    path("about/", views.AboutView.as_view()),

    path("contact/", views.ContactView),

    path("produits/",views.ProduitListView.as_view(),name="lst_prdts"),
    path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),

    path("categories/",views.CategorieListView.as_view(),name="lst_cats"),
    path("categorie/<pk>/" ,views.CategorieDetailView.as_view(), name="dtl_cat"),

    path("status/",views.StatusListView.as_view(),name="lst_stats"),
    path("statut/<pk>/" ,views.StatusDetailView.as_view(), name="dtl_stat"),

    path("rayons/",views.RayonListView.as_view(),name="lst_rys"),
    path("rayon/<pk>/" ,views.RayonDetailView.as_view(), name="dtl_ry"),

    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),

    path('email-sent/',views.mailSend.as_view(),name="email-sent")
]
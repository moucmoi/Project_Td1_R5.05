from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import *
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.forms import BaseModelForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        if self.kwargs.get('param'):
            context['titreh1'] = "Hello " + self.kwargs.get('param')
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    

def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@monprojet.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html",{'titreh1':titreh1, 'form':form})
    

def mailSend(request):
    template_name="monApp/email-send.html"
    return render(request,template_name)
    
class ProductDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')
    
class ProduitUpdateView(UpdateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/update_produit.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)
    
class ProduitCreateView(CreateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/create_produit.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"

    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context

class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context
    


class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rys"

    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des rayons"
        return context

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "ry"

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        return context
    
class RayonUpdateView(UpdateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/update_rayon.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ry = form.save()
        return redirect('dtl_ry', ry.idRayon)
    
class RayonCreateView(CreateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/create_rayon.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ry = form.save()
        return redirect('dtl_ry', ry.idRayon)
    
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('lst_rys')
    


class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "cats"

    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des catégories"
        return context

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categories.html"
    context_object_name = "cat"

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        return context
    
class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/update_categorie.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cat = form.save()
        return redirect('dtl_cat', cat.idCat)
    
class CategorieCreateView(CreateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/create_categorie.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cat = form.save()
        return redirect('dtl_cat', cat.idCat)
    
class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('lst_cats')
    




class StatusListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "stats"

    def get_context_data(self, **kwargs):
        context = super(StatusListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des status"
        return context

class StatusDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "stat"

    def get_context_data(self, **kwargs):
        context = super(StatusDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        return context
    


    
class StatusUpdateView(UpdateView):
    model = Statut
    form_class=StatutForm
    template_name = "monApp/update_status.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        stat = form.save()
        return redirect('dtl_stat', stat.idStatut)
    
class StatusCreateView(CreateView):
    model = Statut
    form_class=StatutForm
    template_name = "monApp/create_status.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        stat = form.save()
        return redirect('dtl_stat', stat.idStatut)
    
class StatusDeleteView(DeleteView):
    model = Statut
    template_name = "monApp/delete_status.html"
    success_url = reverse_lazy('lst_stats')
    


class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'

    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')


class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')
        

class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)




#def produits(request):
#    prdts = Produit.objects.all()
#    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

#def categories(request):
#    cats = Categorie.objects.all()
#    return render(request, 'monApp/list_categories.html',{'cats': cats})


# Create your views here.
#def home(request,param=None):
#    if param is None:
#        return HttpResponse("<h1>Bonjour inconu</h1>")
#    else:
#        return HttpResponse("<h1>Bonjour "+param+"</h1>")

#def contact(request):
#    return render(request, 'monApp/contact.html')

#def about(request):
#    return render(request, 'monApp/about.html')


#def status(request):
#    stats = Statut.objects.all()
#    return render(request, 'monApp/list_statuts.html',{'stats': stats})

#def rayon(request):
#    rys = Rayon.objects.all()
#    return render(request, 'monApp/list_rayons.html',{'rys': rys})
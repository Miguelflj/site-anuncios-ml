from unicodedata import category
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse


from .models import Category
from .models import Ad

def home(request):
    categories = Category.objects.all()
    last_ads = Ad.objects.all()[:12]
 
    return render(request, 'home.html', {'categorias': categories, 'anuncios':last_ads})


def categoria(request,categoria_id):
    categoria = get_object_or_404(Category, id=categoria_id)
    categories = Category.objects.all()
    
    
    ads = Ad.objects.filter(category=categoria)
    
    return render(request, 'home.html', {'categorias': categories, 'anuncios':ads, 'categoria':categoria})


def anuncio(request,anuncio_id):
    anuncio = get_object_or_404(Ad, id=anuncio_id)
    
    return render(request, 'home.html', {'categorias': categories, 'anuncios':ads, 'categoria':categoria})
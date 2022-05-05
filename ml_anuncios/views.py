from django.shortcuts import render
from django.http import HttpResponse


from .models import Category
from .models import Ad

def home(request):
    categories = Category.objects.all()
    last_ads = Ad.objects.all()[:12]
 
    return render(request, 'home.html', {'categorias': categories, 'anuncios':last_ads})
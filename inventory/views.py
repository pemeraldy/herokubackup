from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'inventory/dashboard.html')
    
def products(request):
    products = Product.objects.all()
    available = products.filter(category="Available").count()
    incoming = products.filter(category="Incoming").count()
    outgoing = products.filter(category="Outgoing").count()

    context = {
        'available':available,
        'incoming': incoming,
        'outgoing': outgoing,
        'products': products
    }


    return render(request, 'inventory/products.html', context)
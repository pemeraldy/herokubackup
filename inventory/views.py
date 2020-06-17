from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ProductForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'inventory/dashboard.html', {'products':products})
    
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


def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'inventory/create-product.html', context)


def edit_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products')

    context={'form': form}
    return render(request, 'inventory/create-product.html', context)


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, 'inventory/delete-product.html', context)
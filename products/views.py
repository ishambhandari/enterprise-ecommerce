from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):

    context = Product.objects.all()
    return render(request, 'products.html',context)

def cart(request):
    context = {}
    return render(request, 'cart.html',context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html',context)


def orders(request):
    context = {}
    return render(request, 'orders.html',context)


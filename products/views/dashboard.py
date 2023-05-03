from django.shortcuts import render,get_object_or_404
from products.models import Product, ProductImage
from django.core.paginator import Paginator

def dashboard(request):
    return render(request, 'dashboard.html')

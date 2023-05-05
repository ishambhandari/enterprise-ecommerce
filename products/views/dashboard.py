from django.shortcuts import render,get_object_or_404
from products.models import Product, ProductImage
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.user.is_staff:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'dashboard.html')


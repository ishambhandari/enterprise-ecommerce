from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator


def products(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10) # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'page_obj': page_obj})

# def products_detail(request):



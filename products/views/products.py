from django.shortcuts import render,get_object_or_404
from products.models import Product, ProductImage
from django.core.paginator import Paginator


def products(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10) # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'page_obj': page_obj})

def products_detail(request,id):
    product_instance = get_object_or_404(Product, asin = id) 
    image_urls = ProductImage.objects.filter(product= product_instance)
    return render(request, "product_detail.html", {"product_instance": product_instance , "image_urls":image_urls})





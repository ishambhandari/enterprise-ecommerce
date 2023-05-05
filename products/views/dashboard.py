from django.shortcuts import render,get_object_or_404
from products.models import Product, ProductImage
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from products.models import *
from django.db.models import Count

@login_required
def dashboard(request):
    context = {}
    orders = Order.objects.filter(completed=True)
    order_items = OrderItem.objects.filter(order__in=orders)
    total_price = 0
    total_items_sold = 0
    for order in orders:
        total_price += order.get_cart_total
        total_items_sold += order.get_cart_items


    dictionary = {"ENGLAND":0, "WALES":0, "SCOTLAND":0, "NORTHERN_IRELAND":0}
    addressess = ShippingAddress.objects.all()
    for i in addressess:
        try:
            dictionary[i.country] += 1
        except:
            pass
    print(dictionary)
    context = {
        'order_items': order_items,
        'total_price': total_price,
        'total_items_sold': total_items_sold,
        'dictionary':dictionary
    }
    return render(request, 'dashboard.html', context)

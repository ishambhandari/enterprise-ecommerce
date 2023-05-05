from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product, ProductImage, Order, OrderItem, ShippingAddress
from django.http import JsonResponse
from products.forms import ShippingAddressForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import json
from django.http import HttpResponseForbidden


def handler404(request, *args, **argv):
    response = render(request, '404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def error_403(request, exception):
    return HttpResponseForbidden(render(request, '403.html'))


@login_required(login_url='login', redirect_field_name=None)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}

    return render(request, 'cart.html', context)


@login_required(login_url='login', redirect_field_name=None)
def update_cart(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        customer = request.user
        product = Product.objects.get(asin=productId)
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()
        if orderItem.quantity <= 0:
            orderItem.delete()
        return JsonResponse("item added", safe=False)
    else:
        return JsonResponse("Not logged in", safe=False)


@login_required(login_url='login', redirect_field_name=None)
def checkout(request):
    form = ShippingAddressForm()
    transaction_id = datetime.now().timestamp()
    if request.method == 'POST':
        order, created = Order.objects.get_or_create(customer=request.user, completed=False)
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            shipping_address = ShippingAddress.objects.create(
                customer=request.user,
                order=order,
                address=data['address'],
                country=data['country']
            )
            order.transaction_id = transaction_id
            order.completed = True
            order.save()
            return redirect('products')
        else:
            print(form.errors)
            print(form.cleaned_data)
            return redirect('products')

    return render(request, 'checkout.html', {'form': form})

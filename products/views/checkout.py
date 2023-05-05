from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime
from .forms import ShippingAddressForm
from .models import Order, ShippingAddress


def checkout(request):
    form = ShippingAddressForm()
    context = {'form': form}
    transaction_id = datetime.now().timestamp()
    order, created = Order.objects.get_or_create(customer=request.user, completed=False)
    return render(request, 'checkout.html', context)

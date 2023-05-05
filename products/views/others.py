from django.shortcuts import render,get_object_or_404, redirect

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Order

@login_required()
def detail(request):
    orders = Order.objects.filter(customer=request.user, completed=True)
    total_spending = sum([order.get_cart_total for order in orders])
    context = {'total_spending': total_spending, 'user':request.user}
    return render(request, 'accountdetail.html', context)


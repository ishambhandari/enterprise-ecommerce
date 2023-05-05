from django.contrib import admin
from django.urls import path, include
from products.views import products, dashboard, cart, others

urlpatterns = [
    path('', products.products, name='products'),
    path('list/<str:id>/', products.products_detail, name='products_detail'),
    path('dashboard/', dashboard.dashboard, name='dashboard'),
    path('cart/', cart.cart, name='cart'),
    path('update-cart/', cart.update_cart, name='update_cart'),
    path('checkout/', cart.checkout, name='checkout'),
    path('detail/', others.detail, name='account-detail'),
    # path('orders', views.orders, name='orders'),
]

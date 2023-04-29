from django.contrib import admin
from django.urls import path,include
from . import views
from products.views import products

urlpatterns = [
    path('', views.products.products, name = "products"),
    # path('cart/', views.cart, name = "cart"),
    # path('checkout/', views.checkout, name = "checkout"),
    # path('orders', views.orders, name = "orders"),
]

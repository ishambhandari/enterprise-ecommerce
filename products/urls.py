from django.contrib import admin
from django.urls import path, include
from products.views import products, dashboard

urlpatterns = [
    path('', products.products, name='products'),
    path('list/<str:id>/', products.products_detail, name='products_detail'),
    path('dashboard/', dashboard.dashboard, name='dashboard'),
    # path('cart/', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('orders', views.orders, name='orders'),
]

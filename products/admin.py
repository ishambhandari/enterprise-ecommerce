from django.contrib import admin
from .models import Product, ProductImage, Features, Order, OrderItem, ShippingAddress

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Features)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

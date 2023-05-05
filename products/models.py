from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    asin = models.CharField(max_length=100, primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10.0)
    brand = models.CharField(max_length=100)
    display_image = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.asin} {self.price}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product.title}, {self.image_url}"

class Features(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.product.title}, {self.feature}"

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.id}"

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = 0
        for items in orderitems:
            total = sum([items.get_total])
        return total

    
    @property
    def get_cart_items(self):
        total = 0
        orderitems = self.orderitem_set.all()
        for items in orderitems:
            total = sum([items.quantity])
        return total



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True) 

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    class Countries(models.TextChoices):
        ENGLAND = 'ENGLAND',
        SCOTLAND = 'SCOTLAND', 
        WALES = 'WALES',
        NORTHERN_IRELAND = 'NORTHERN_IRELAND'

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=500, null=True)
    country = models.CharField(max_length=20, choices=Countries.choices)

    def __str__(self):
        return f"{self.address}, {self.country}"

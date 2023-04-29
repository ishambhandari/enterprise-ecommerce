from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Product(models.Model):
    asin = models.CharField(max_length = 100, primary_key = True, unique = True)
    title = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 5, decimal_places = 2, default = 10.0)
    brand = models.CharField(max_length = 100)
    display_image = models.CharField(max_length = 100, null = True)

    def __str__(self):
        return f"{self.asin} {self.price}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    image_url = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.product.title}, {self.image_url}"

class Features(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    feature = models.CharField(max_length = 500)


    def __str__(self):
        return f"{self.product.title}, {self.feature}"


# class Cart(models.Model):
    






        






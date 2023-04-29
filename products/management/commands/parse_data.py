import json
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from products.models import Product, ProductImage, Features
import random

class Command(BaseCommand):
    help = 'Loading from json file'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        ProductImage.objects.all().delete()
        Features.objects.all().delete()
        base_dir = Path(__file__).resolve().parent.parent.parent.parent.parent
        with open (str(base_dir)+ '/dataset.json') as f:
            lis = []
            data = json.load(f)
            for i in data:
                try:
                    product_item = Product.objects.create(
                            asin = i["asin"],
                            title = i["title"],
                            price = random.uniform(25, 250),
                            brand = i["brand"],
                            display_image = i["images_list"][0]
                            )
                except:
                    product_item = Product.objects.create(
                            asin = i["asin"],
                            title = i["title"],
                            price = random.uniform(25, 250),
                            brand = i["brand"],
                            display_image = 'https://thumbs.dreamstime.com/z/no-image-available-icon-photo-camera-flat-vector-illustration-132483141.jpg'
                            )

                product_item.save()
                print(product_item)
                
                for img in i["images_list"]:
                    product_image = ProductImage.objects.create(
                            product = product_item, 
                            image_url = img
                            )
                    product_image.save()

                for feature in i["features"]:
                    feature_list = Features.objects.create(
                            product = product_item, 
                            feature = feature
                            )
                    feature_list.save()






# Generated by Django 4.2 on 2023-04-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='display_image',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
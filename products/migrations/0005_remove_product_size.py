# Generated by Django 4.1.1 on 2022-09-16 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_product_size"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="size",),
    ]

# Generated by Django 4.1.1 on 2022-09-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]

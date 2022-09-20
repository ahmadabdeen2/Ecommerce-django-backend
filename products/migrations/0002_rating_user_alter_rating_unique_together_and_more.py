# Generated by Django 4.1.1 on 2022-09-16 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="rating", unique_together={("user", "product")},
        ),
        migrations.AlterIndexTogether(
            name="rating", index_together={("user", "product")},
        ),
    ]

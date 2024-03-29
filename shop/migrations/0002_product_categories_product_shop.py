# Generated by Django 4.2.7 on 2024-02-25 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="categories",
            field=models.ManyToManyField(related_name="product", to="shop.category"),
        ),
        migrations.AddField(
            model_name="product",
            name="shop",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to="shop.shop"),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.7 on 2024-02-26 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_product_categories_product_shop"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image_url",
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
    ]

from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model


class Shop(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='media/', blank=True, null=True)
    active = models.BooleanField(default=False)
    
    User = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='product_user')

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField('Category', related_name='product')

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    parent = models.ForeignKey(
        "self", on_delete=models.SET_NULL, related_name="children", blank=True, null=True
    )

    def __str__(self):
        return self.title

from django.db import models
from utils.models import BaseModel


class Shop(BaseModel):
    title = models.CharField(max_length=255)
    image_url = models.URLField()

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='media/', blank=True, null=True)
    active = models.BooleanField(default=False)
    
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField('Category', related_name='product',blank=True, null=True)


class Category(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children")

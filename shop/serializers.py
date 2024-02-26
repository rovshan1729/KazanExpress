from rest_framework import serializers
from .models import Shop, Product, Category


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            "id",
            "title",
            "image_url",
            "created_at",
            "updated_at",
        )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "amount",
            "price",
            "image",
            "active",
            "created_at",
            "updated_at",
        )
        read_only_fields = ['id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "description",
            "created_at",
            "updated_at",
        )

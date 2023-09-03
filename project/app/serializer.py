from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "slug", "title", "category", "description", "price", "image")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", 'id', "parent_id",)


class NewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['seller', 'slug']

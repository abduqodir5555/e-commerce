from rest_framework import serializers

from .models import *
from common.serializers import MediaSerializer

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("image", "lft", "rght", "tree_id", "level")


class ProductListSerializer(serializers.ModelSerializer):
    thumbnail = MediaSerializer()
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category', 'in_stock', 'brand', 'discount', 'thumbnail')

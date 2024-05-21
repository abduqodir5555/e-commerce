from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CategoryListSerializer, ProductListSerializer, ProductColorSerializer, ProductSizeSerializer
from .models import Category, Product, ProductColour, ProductSize


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = None


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'colours', 'sizes']

    def get_queryset(self):
        min_price = self.request.query_params.get("min_price", None)
        max_price = self.request.query_params.get("max_price", None)
        if min_price and max_price:
            queryset = self.queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price is None and max_price:
            queryset = self.queryset.filter(price__lte=max_price)

        elif max_price is None and min_price:
            queryset = self.queryset.filter(price__gte=min_price)
        else:
            queryset = self.queryset.all()
        return queryset


class ProductColorView(ListAPIView):
    queryset = ProductColour.objects.all()
    serializer_class = ProductColorSerializer


class ProductSizeView(ListAPIView):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer

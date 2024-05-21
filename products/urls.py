from django.urls import path

from .views import CategoryListAPIView, ProductListAPIView, ProductColorView, ProductSizeView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('colours/', ProductColorView.as_view(), name='colour'),
    path('sizes/', ProductSizeView.as_view(), name='size')
]
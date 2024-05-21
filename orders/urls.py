from django.urls import path

from orders.views import AddToCartView, UpdateUserCartItem

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view()),
    path('cart-item-update/<int:productid>/', UpdateUserCartItem.as_view())
]
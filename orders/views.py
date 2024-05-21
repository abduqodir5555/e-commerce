from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics

from orders.models import CartItem
from orders.serializers import AddToCartSerilizer, UpdateCartItemSerializer
from products.models import Product


class AddToCartView(APIView):
    serializer_class = AddToCartSerilizer
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        try:
            serializer = self.serializer_class(data = request.data)
            if not serializer.is_valid():
                return Response(data = {"message":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
            data = serializer.validated_data
            product = Product.objects.get(id=data.get('product_id'))
            item = CartItem.objects.create(user=request.user, quantity=data.get('quantity'), product=product)
            return Response(data={"message":"cart item added", "result":item.id}, status=status.HTTP_201_CREATED)

        except Product.DoesNotExist:
            return Response(data={"message":"Product does not found"}, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserCartItem(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = UpdateCartItemSerializer
    lookup_field = 'productid'
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        cart_item = CartItem.objects.get(user=self.request.user, product=self.kwargs.get(self.lookup_field))
        return cart_item


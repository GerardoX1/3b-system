from inventory.models import Orders, Products
from inventory.serializers import OrdersSerializer, ProductsSerializer
from rest_framework import generics


class ListProducts(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class UpdateProducts(generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ListOrders(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

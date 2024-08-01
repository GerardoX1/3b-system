from inventory.models import Orders, Products
from inventory.serializers import OrdersSerializer, ProductsSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView


class CreateProducts(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class UpdateProducts(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CreateOrders(CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

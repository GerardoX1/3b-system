from inventory.models import Orders, Products
from inventory.serializers import (
    AddStockSerializer,
    OrdersSerializer,
    ProductsSerializer,
)
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response


class CreateProducts(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class UpdateProducts(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = AddStockSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer, instance)
            return Response({"status": "stock updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer, instance):
        serializer.update(instance, serializer.validated_data)


class CreateOrders(CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"status": "purchase made"}, status=status.HTTP_201_CREATED)

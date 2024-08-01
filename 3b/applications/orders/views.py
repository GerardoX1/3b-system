from applications.orders.models import Orders
from applications.orders.serializers import OrdersSerializer
from rest_framework import generics


class ListOrders(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
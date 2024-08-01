from applications.products.models import Products
from applications.products.serializers import ProductsSerializer
from rest_framework import generics


class ListProducts(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class UpdateProducts(generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
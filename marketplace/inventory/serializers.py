from inventory.models import Orders, Products
from rest_framework import serializers


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class AddStockSerializer(serializers.Serializer):
    add_stock = serializers.IntegerField(min_value=1)

    def update(self, instance, validated_data):
        add_stock = validated_data.get("add_stock")
        instance.stock += add_stock
        instance.save()
        return instance


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"

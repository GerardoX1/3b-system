from inventory.constants import OUT
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
    product_id = serializers.UUIDField(write_only=True)
    quantity = serializers.IntegerField(write_only=True)

    class Meta:
        model = Orders
        fields = ["product_id", "quantity", "created_at"]

    def validate(self, data):
        product_id = data.get("product_id")
        quantity = data.get("quantity")

        try:
            product = Products.objects.get(_id=product_id)
        except Products.DoesNotExist:
            raise serializers.ValidationError("Product not found.")

        if product.stock < quantity:
            raise serializers.ValidationError("Not enough stock available.")

        data["product"] = product
        data["total_cost"] = product.unit_price * quantity
        return data

    def create(self, validated_data):
        product = validated_data.get("product")
        quantity = validated_data.get("quantity")

        # Reduce the stock of the product
        product.stock -= quantity
        product.save()

        # Create the order
        order = Orders.objects.create(
            product=product,
            quantity=quantity,
            transaction_type=OUT,
            total_cost=validated_data.get("total_cost"),
        )
        return order

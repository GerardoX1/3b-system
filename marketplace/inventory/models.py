import uuid

from django.db import models
from inventory.constants import CATEGORY_TYPES, IN, OUT, TRANSACTION_TYPES


class Products(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_name = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_TYPES)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)

    def stock_out(self, quantity):
        if quantity > self.stock:
            raise ValueError("Not enough stock.")
        self.stock -= quantity
        self.save(update_fields=["stock"])

    def __str__(self):
        return self.display_name


class Orders(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, default=None)

    def save(self, *args, **kwargs):
        if self.transaction_type == OUT:
            self.product.stock_out(self.quantity)

        super().save(*args, **kwargs)

    def __str__(self):
        return self._id

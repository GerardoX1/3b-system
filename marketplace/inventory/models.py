import uuid

from django.db import models


class Products(models.Model):
    CATEGORY_TYPES = [
        ("Electronics", "Electronics"),
        ("Home & Kitchen", "Home & Kitchen"),
        ("Books", "Books"),
        ("Beauty & Personal Care", "Beauty & Personal Care"),
        ("Clothing", "Clothing"),
        ("Sports & Outdoors", "Sports & Outdoors"),
        ("Toys & Games", "Toys & Games"),
    ]
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_name = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_TYPES)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.display_name


class Orders(models.Model):
    TRANSACTION_TYPES = [
        ("in", "In"),
        ("out", "Out"),
    ]
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self._id

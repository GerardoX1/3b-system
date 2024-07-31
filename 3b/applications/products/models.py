from django.db import models
import uuid


class Products(models.Model):
    CATEGORY_TYPES = [
        ('Electronics', 'Electronics'),
        ('Home & Kitchen', 'Home & Kitchen'),
        ('Books', 'Books'),
        ('Beauty & Personal Care', 'Beauty & Personal Care'),
        ('Clothing', 'Clothing'),
        ('Sports & Outdoors', 'Sports & Outdoors'),
        ('Toys & Games', 'Toys & Games'),
    ]
    _id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    sku = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_name = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_TYPES)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.display_name

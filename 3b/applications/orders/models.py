from django.db import models
import uuid
from applications.products.models import Products


class Orders(models.Model):
    TRANSACTION_TYPES = [
        ('in', 'In'),
        ('out', 'Out'),
    ]
    _id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(
        max_length=15,
        choices=TRANSACTION_TYPES
        )
    quantity = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        default=None
        )

    def __str__(self):
        return self._id

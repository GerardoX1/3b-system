from django.db.models.signals import post_save
from django.dispatch import receiver
from inventory.constants import IN
from inventory.models import Orders, Products


@receiver(post_save, sender=Products)
def create_order(sender, instance, created, **kwargs):
    if created:
        Orders.objects.create(
            transaction_type=IN,
            quantity=instance.stock,
            total_cost=instance.stock * instance.unit_price,
            product=instance,
        )

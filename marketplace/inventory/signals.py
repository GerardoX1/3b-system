from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from inventory.constants import IN, OUT
from inventory.models import Orders, Products


@receiver(post_save, sender=Products)
def create_order(sender, instance, created, **kwargs):
    if created:
        Orders.objects.create(
            transaction_type=IN,
            quantity=instance.stock,
            total_cost=instance.stock * instance.unit_price,
            product=instance.product,
        )


@receiver(pre_save, sender=Products)
def update_order(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Products.objects.get(pk=instance.pk)
        except Products.DoesNotExist:
            raise ValueError("Invalid product.")

        if old_instance.stock != instance.stock:
            Orders.objects.create(
                transaction_type=OUT,
                quantity=instance.stock - old_instance.stock,
                total_cost=(instance.stock - old_instance.stock) * instance.unit_price,
                product=instance.product,
            )

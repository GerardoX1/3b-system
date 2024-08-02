import logging
from datetime import datetime

from celery import shared_task
from inventory.models import Products


@shared_task
def check_product_stock():
    low_stock_products = Products.objects.filter(stock__lt=10)
    for product in low_stock_products:
        logging.warning(
            f"El stock del producto "
            f"{product.display_name} (ID: {product._id}) "
            "es inferior a 10 unidades."
        )

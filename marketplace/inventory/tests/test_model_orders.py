from uuid import NAMESPACE_OID, uuid5

import pytest
from django.utils import timezone
from inventory.models import Orders, Products


def uuid_by_params(*args):
    value = "#".join(map(str, args))
    return str(uuid5(namespace=NAMESPACE_OID, name=value))


@pytest.mark.django_db
def test_create_order_success():
    product = Products.objects.create(
        sku="1234-2345-3456-4567",
        display_name="Test product 01",
        description="A product for testing purposes",
        category="Electronics",
        unit_price=100,
        stock=100,
    )
    order = Orders.objects.create(
        transaction_type="IN", quantity=10, total_cost=50, product=product
    )
    assert order.created_at <= timezone.now()
    assert order.transaction_type == "IN"
    assert order.quantity == 10
    assert order.total_cost == 50
    assert order.product == product

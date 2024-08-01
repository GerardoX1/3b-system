import pytest
from applications.inventory.models import Products
from django.utils import timezone


@pytest.mark.django_db
def test_create_product_success():
    product = Products.objects.create(
        sku="1234-2345-3456-4567",
        display_name="Test product 01",
        description="A product for testing purposes",
        category="Electronics",
        unit_price=100,
        stock=100,
    )
    assert product.display_name == "Test product 01"
    assert product.description == "A product for testing purposes"
    assert product.created_at <= timezone.now()
    assert product.updated_at <= timezone.now()
    assert product.category == "Electronics"
    assert product.unit_price == 100
    assert product.stock == 100


@pytest.mark.django_db
def test_product_string_representation():
    product = Products.objects.create(
        sku="1234-2345-3456-4567",
        display_name="Test product 02",
        description="Another test product",
        category="Electronics",
        unit_price=10,
        stock=10,
    )
    assert str(product) == "Test product 02"

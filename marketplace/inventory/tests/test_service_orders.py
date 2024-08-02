import pytest
from django.urls import reverse
from inventory.models import Orders, Products
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestOrderPostEndpoint:

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def product(self):
        return Products.objects.create(
            id="bf64d0d5-9e35-44f5-846a-efbde318323e",
            name="Test Product",
            description="A product for testing purposes",
            price=100.0,
            stock=100,
        )

    def test_create_order_success(self, api_client, product):
        url = reverse("product-pull")
        data = {"product_id": str(product.id), "quantity": 50}
        response = api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_201_CREATED

        order = Orders.objects.get(product=product)
        assert order.product == product
        assert order.quantity == 50

    def test_create_order_missing_fields(self, api_client):
        url = reverse("product-pull")
        data = {
            "product_id": "bf64d0d5-9e35-44f5-846a-efbde318323e"
            # need quantity
        }
        response = api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert Orders.objects.count() == 0

    def test_create_order_invalid_data(self, api_client, product):
        url = reverse("product-pull")
        data = {"product_id": str(product.id), "quantity": -10}  # Invalid quantity
        response = api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert Orders.objects.count() == 0

    def test_create_order_nonexistent_product(self, api_client):
        url = reverse("product-pull")
        data = {"product_id": "nonexistent-uuid", "quantity": 50}
        response = api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Orders.objects.count() == 0

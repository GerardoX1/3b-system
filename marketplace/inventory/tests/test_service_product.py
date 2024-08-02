import pytest
from django.urls import reverse
from inventory.models import Products
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestProductPostEndpoint:

    @pytest.fixture
    def api_client(self):
        return APIClient()

    def test_create_product_success(self, api_client):
        url = reverse("product-create")
        data = {
            "sku": "2345-3456-4567-5678",
            "display_name": "Test product 02",
            "description": "A product for testing purposes",
            "category": "Electronics",
            "unit_price": 99,
        }
        response = api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_201_CREATED

        product = Products.objects.get(sku="2345-3456-4567-5678")
        assert product.display_name == "Test product 02"
        assert product.description == "A product for testing purposes"
        assert product.category == "Electronics"
        assert product.unit_price == 99

    def test_create_product_missing_fields(self, api_client):
        url = reverse("product-create")
        data = {
            "sku": "2345-3456-4567-5678",
            "display_name": "Test product 02",
            # need description, category, and unit_price
        }
        response = api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Products.objects.count() == 0

    def test_create_product_invalid_data(self, api_client):
        url = reverse("product-create")
        data = {
            "sku": "2345-3456-4567-5678",
            "display_name": "Test product 02",
            "description": "A product for testing purposes",
            "category": "Electronics",
            "unit_price": -10,  # Invalid unit price
        }
        response = api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Products.objects.count() == 0

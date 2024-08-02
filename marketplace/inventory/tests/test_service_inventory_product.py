import pytest
from django.urls import reverse
from inventory.models import Products
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestInventoryPatchEndpoint:

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def products(self):
        return Products.objects.create(
            name="Test Product",
            description="A product for testing",
            price=10.0,
            stock=50,
        )

    def test_patch_inventory_success(self, api_client, product):
        url = reverse("product-push", args=[product.id])
        data = {"add_stock": 10}
        response = api_client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK

    def test_patch_inventory_invalid_data(self, api_client, product):
        url = reverse("product-push", args=[product.id])
        data = {"add_stock": -10}  # Invalid quantity
        response = api_client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_patch_inventory_nonexistent_product(self, api_client):
        url = reverse("product-push", args=[9999])  # Nonexistent product ID
        data = {"add_stock": 200}
        response = api_client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_404_NOT_FOUND

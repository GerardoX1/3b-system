from django.urls import path
from inventory.views import CreateOrders, CreateProducts, UpdateProducts

urlpatterns = [
    path("products", CreateProducts.as_view(), name="product-create"),
    path("inventories/product/<str:pk>", UpdateProducts.as_view(), name="product-push"),
    path("orders", CreateOrders.as_view(), name="product-pull"),
]

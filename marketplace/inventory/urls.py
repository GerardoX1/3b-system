from django.urls import path
from inventory.views import CreateOrders, CreateProducts, UpdateProducts

urlpatterns = [
    path("products", CreateProducts.as_view()),
    path("inventories/product/<str:pk>", UpdateProducts.as_view()),
    path("orders", CreateOrders.as_view()),
]

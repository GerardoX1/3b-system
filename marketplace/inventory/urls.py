from django.urls import path
from inventory.views import ListOrders, ListProducts, UpdateProducts

urlpatterns = [
    path("products", ListProducts.as_view()),
    path("inventories/product/<str:pk>", UpdateProducts.as_view()),
    path("orders", ListOrders.as_view()),
]

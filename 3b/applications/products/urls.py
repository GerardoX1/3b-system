from applications.products.views import ListProducts, UpdateProducts
from django.urls import path

urlpatterns = [
    path("", ListProducts.as_view()),
    path("<str:pk>", UpdateProducts.as_view()),
]

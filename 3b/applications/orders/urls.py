from applications.orders.views import ListOrders
from django.urls import path

urlpatterns = [
    path("", ListOrders.as_view()),
]

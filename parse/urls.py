from django.urls import path
from .views import api_products, products

urlpatterns = [
    path('add/', products),
    path('add/products/', api_products),
]
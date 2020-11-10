from django.urls import path
from .views import api_products, products, api_tree_category

urlpatterns = [
    path('add/', products),
    path('add/products/', api_products),
    path('add/category/', api_tree_category),
]
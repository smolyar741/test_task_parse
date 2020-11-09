from rest_framework import serializers, exceptions
from django.contrib.auth import models

from .models import Product
from rest_framework.exceptions import ValidationError


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'title',
            'category',
            'url', 
            'image_url',
        )
        model = Product
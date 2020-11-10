from rest_framework import serializers, exceptions
from django.contrib.auth import models

from .models import Product, TreeCategory
from rest_framework.exceptions import ValidationError


class RecursiveField(serializers.Serializer):
    def to_native(self, value):
        return self.parent.to_native(value)


class TreeCategorySerializer(serializers.ModelSerializer):
    parent = RecursiveField(required=False)

    class Meta:
        fields = (
            'category',
            'parent',
        )
        model = TreeCategory


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'title',
            'category',
            'url', 
            'image_url',
        )
        model = Product
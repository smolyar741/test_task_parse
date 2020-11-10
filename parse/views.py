import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, TreeCategory
from .serializers import ProductSerializer, TreeCategorySerializer


def index(request):
    pass


@api_view(['GET'])
def api_tree_category(request):
    if request.method == 'GET':
        category = TreeCategory.objects.all()
        serializer = TreeCategorySerializer(category, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


def products(request):
    with open('wb.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    for i in data:
        print('Товар:',i)
        product = Product(
            title=i['title'], 
            category=i['category'], 
            url=i['url'], 
            image_url=i['image_url'])
        product.save()
    return HttpResponse('\n'.join(str(data)))
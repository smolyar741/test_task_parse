from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .forms import ProductForm
from .models import Product, TreeCategory


@admin.register(TreeCategory)
class TreeCategoryAdmin(MPTTModelAdmin):
    list_display = ('pk', 'category', 'parent')
    empty_value_display = '-пусто-'
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'url', 'image_url')
    empty_value_display = '-пусто-'
    form = ProductForm
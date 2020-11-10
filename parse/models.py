from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class TreeCategory(MPTTModel):
    category = models.CharField(max_length=50, unique=True, verbose_name='Категория товара')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родитель')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class MPTTModel:
        level_attr = 'mptt_level'
        order_insertion_by=['category']

    def __unicode__(self):
        return self.category
        

class Product(models.Model):
    title = models.TextField(verbose_name='Название')
    category = models.TextField(verbose_name='Категория товара')
    url = models.URLField(verbose_name='ссылка на товар')
    image_url = models.URLField(verbose_name='ссылка на картинку')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'





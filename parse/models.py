from django.db import models


class Product(models.Model):
    title = models.TextField(verbose_name='Название')
    category = models.TextField(verbose_name='Категория товара')
    url = models.URLField(verbose_name='ссылка на товар')
    image_url = models.URLField(verbose_name='ссылка на картинку')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'





# Generated by Django 3.1.2 on 2020-11-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0005_auto_20201110_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Категория товара'),
        ),
    ]
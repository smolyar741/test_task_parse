# Generated by Django 3.1.2 on 2020-11-10 06:25

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0010_auto_20201110_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parse.treecategory', verbose_name='Категория товара'),
        ),
    ]

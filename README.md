# WB-project

Тестовый проект.
Парсинг сайта Wildberries и отдача данных во фронт с помощью DRF.

## Файлы.

*wb_parse.py - парсер данны.*

>В приложении Parse создана модель объекта парсинга и модель древовидной структуры категорий. 
>Для моделей прописана админка и форма.
>Создан сериализатор для перевода данных в json.
>Во вью реализована передача данных из json в базу данных Django.
>Передача объектов парсинга во фронт по урл http://127.0.0.1:8000/add/products/

## Требования

Перед запуском работы проверьте наличие 
[Python](https://www.python.org/downloads/),
[Django](https://www.djangoproject.com/), 
[Django-Rest-Framework](https://www.django-rest-framework.org/)

## Установка 
*Клонируйте репозиторий на локальный компьютер*

```
$ python3 -m venv venv
$ source venv/bin/activate 
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

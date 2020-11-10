# WB-project

Тестовый проект.
Парсинг сайта Wildberries и отдача данных во фронт с помощью DRF.

## Файлы.
wb_parse.py - парсер данных и запись в csv файл.
converter.py - конвертер данных из csv файла в json.

В приложении Parse создана модель данных. 
Прописана админка и форма.
Во вью реализована передача данных из json в базу данных Django.
Передача json во фронт по урл http://127.0.0.1:8000/add/products/

## Требования

Перед запуском работы проверьте наличие 
[Python](https://www.python.org/downloads/),
[Django](https://www.djangoproject.com/), 
[Django-Rest-Framework](https://www.django-rest-framework.org/)

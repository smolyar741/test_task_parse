import json
from django.http import HttpResponse
from parse.models import Product



def products(request):
    with open('wb.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    for i in data:
        print('Товар:',i)
        product = Product(title=i['title'], category=i['category'], url=i['url'], image_url=i['image_url'])
        product.save()
    return HttpResponse('\n'.join(str(data)))
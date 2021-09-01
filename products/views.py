from django.shortcuts import render
import os
import json

JSON_DIR = os.path.dirname(__file__)


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
        'user': 'username',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'user': 'username',
    }
    path_file = os.path.join(JSON_DIR, 'fixtures/goods.json')
    with open(path_file, 'rb') as file:
        context['products'] = json.load(file, encoding='utf-8')

    return render(request, 'products/products.html', context)

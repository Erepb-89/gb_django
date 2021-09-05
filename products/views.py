from django.shortcuts import render
import os
import json

from products.models import Product, ProductsCategory

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
        'products': Product.objects.all(),
        'category': ProductsCategory.objects.all(),
        }
    # context['products'] = Product.objects.all()

    return render(request, 'products/products.html', context)

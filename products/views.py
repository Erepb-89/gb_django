from django.shortcuts import render
import os
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Product, ProductsCategory

JSON_DIR = os.path.dirname(__file__)


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, id=None, page=1):
    products = Product.objects.filter(category_id=id) if id is not None and id != 0 else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'GeekShop - Каталог',
        'category': ProductsCategory.objects.all(),
        'products': products_paginator
    }

    return render(request, 'products/products.html', context)

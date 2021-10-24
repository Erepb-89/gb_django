from django.db.models import F
from django.shortcuts import render, HttpResponseRedirect

from django.db import connection

from products.models import Product
from baskets.models import Basket
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.
@login_required
def baskets_add(request, id):
    product = Product.objects.get(id=id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        baskets = baskets.first()
        # baskets.quantity += 1
        baskets.quantity = F('quantity') + 1
        baskets.save()

        # update_queries = list(filter(lambda x: 'UPDATE' in x['sql'], connection.queries))
        # print(f'basket_add {update_queries} ')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def baskets_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user=request.user).select_related()
        context = {
            'baskets': baskets
        }
        result = render_to_string('baskets/baskets.html', context, request=request)
        return JsonResponse({'result': result})


@login_required
def baskets_remove(request, id):
    Basket.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

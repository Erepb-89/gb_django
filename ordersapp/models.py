from django.db import models
from django.conf import settings
from products.models import Product


# Create your models here.

class Order(models.Model):
    FORMING = 'FM'
    SEND_TO_PROCEED = 'STP'
    PAID = 'PD'
    PROCEEDED = 'PRD'
    READY = 'RD'
    CANCEL = 'CNC'

    ORDER_CHOICES = (
        (FORMING, 'Формируется'),
        (SEND_TO_PROCEED, 'Отправлено в обработку'),
        (PAID, 'Оплачено'),
        (PROCEEDED, 'Обрабатывается'),
        (READY, 'Готов к выдаче'),
        (CANCEL, 'Отмена заказа'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='create', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='update', auto_now=True)
    status = models.CharField(verbose_name='status', max_length=3, default=FORMING, choices=ORDER_CHOICES)
    is_active = models.BooleanField(verbose_name='active', default=True)

    def __str__(self):
        return f'Текущий заказ {self.pk}'

    @property
    def _items(self):
        return self.orderitems.select_related()

    def get_total_quantity(self):
        return sum(list(map(lambda x: x.quantity, self._items)))

    def get_total_cost(self):
        return sum(list(map(lambda x: x.get_product_cost(), self._items)))

    def delete(self, using=None, keep_parents=False):
        for item in self._items:
            item.product.quantity += item.quantity
            item.product.save()
        self.is_active = False
        self.save()

    def get_summary(self):
        items = self.orderitems.select_related()
        return {
            'total_cost': sum(list(map(lambda x: x.get_product_cost(), items))),
            'total_quantity': sum(list(map(lambda x: x.quantity, items))),
        }


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='продукты', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'Текущий заказ {self.pk}'

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.get(pk=pk).quantity

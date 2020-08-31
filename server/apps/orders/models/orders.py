from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from apps.dishes.models import Dish


class Status(models.Model):
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

    def __str__(self):
        return self.name


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    comments = models.TextField(max_length=1000, blank=True,
                                null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10,
                                      decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Заказ №{self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class DishInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name='Номер заказа')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1,
                                             verbose_name='Количество')
    price_per_item = models.DecimalField(max_digits=10,
                                         decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10,
                                      decimal_places=2, default=0)

    def __str__(self):
        return f'{self.dish.name} {self.count} шт.'

    class Meta:
        verbose_name = 'Блюдо в заказе'
        verbose_name_plural = 'Блюда в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.dish.price
        self.price_per_item = price_per_item
        self.total_price = price_per_item * self.count
        super(DishInOrder, self).save(*args, **kwargs)


def dish_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    order_total_price = 0
    all_dish_in_order = DishInOrder.objects.filter(order=order)
    for item in all_dish_in_order:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(dish_in_order_post_save, DishInOrder)

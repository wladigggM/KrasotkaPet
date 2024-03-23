from django.db import models

from mainApp.models import Item
from users.models import User


# Create your models here.

class Order(models.Model):

    STATUS_CHOICES = (
        ('processing', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменен'),
    )

    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Пользователь",
                             default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    requires_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
    delivery_address = models.CharField(max_length=150, null=True, blank=True, verbose_name="Адрес доставки")
    payment_on_get = models.BooleanField(default=False, verbose_name='Оплата при получении')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='processing', verbose_name='Статус заказа')

    class Meta:
        db_table = "order"
        verbose_name = "Заказы"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ №{self.pk} | Покупатель {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(to=Item, on_delete=models.SET_DEFAULT, null=True, verbose_name="Товар", default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кол-во")
    size = models.IntegerField(default=0, verbose_name="Размер")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданый товар"
        verbose_name_plural = "Проданые товары"

    def __str__(self):
        return f'{self.order} | {self.product} | дата продажи {self.created_timestamp}'

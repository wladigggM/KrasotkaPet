from django.db import models

# Create your models here.

from users.models import User
from django.db import models
from mainApp.models import Item


# Create your models here.

class CartQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='пользователь')
    product = models.ForeignKey(to=Item, on_delete=models.CASCADE, verbose_name='товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='кол-во')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
    new_params = models.CharField(max_length=32, null=True, blank=True)
    size = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    objects = CartQueryset().as_manager()

    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f'Корзина {self.user}| Товар {self.product.name}| Кол-во {self.quantity}'
        # return f'Корзина {self.user.username}| Товар {self.product.name}| Кол-во {self.quantity}'

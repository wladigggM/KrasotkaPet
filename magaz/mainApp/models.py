from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug_name = models.CharField(max_length=100, default='slug_name', verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(default=None, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='items/%Y/%m/%d/', blank=True, verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    slug_name = models.CharField(max_length=100, default='slug_name', verbose_name='Слаг (форен кей)')
    item_slug = models.CharField(max_length=100, default='item_slug', verbose_name='Слаг (предмета)')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2,verbose_name='Скидка')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.category:
            self.category = Category.objects.get(name='Домашняя одежда')
        super().save(*args, **kwargs)

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)
        return self.price
    class Meta:
        verbose_name = 'Вещи'
        verbose_name_plural = 'Вещи'
        ordering = ['created_at', 'updated_at']


class Reviews(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.CharField(max_length=255, verbose_name='Email')
    rating = models.CharField(max_length=255, verbose_name='Рейтинг')
    comment = models.TextField(max_length=255, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

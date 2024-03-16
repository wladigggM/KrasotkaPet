from django.db import models
from django.template.defaultfilters import slugify

from transliterate import translit


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug_name = models.SlugField(max_length=100, unique=True, verbose_name='Слаг', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug_name or translit(str(self.name), 'ru', reversed=True) != self.slug_name:
            slug_name = translit(str(self.name), 'ru', reversed=True)
            self.slug_name = slugify(slug_name)

            super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Size(models.Model):
    size_name = models.IntegerField(verbose_name='Размер')

    def __str__(self):
        return str(self.size_name)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(default=None, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='items/%Y/%m/%d/', blank=True, verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    slug_name = models.SlugField(max_length=100, verbose_name='Слаг (форен кей)', blank=True)
    item_slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг (предмета))', blank=True)
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка')
    size = models.ManyToManyField(Size, verbose_name='Размеры')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.category:
            self.category = Category.objects.get(name='Домашняя одежда')

        if not self.item_slug or translit(str(self.name), 'ru', reversed=True) != self.item_slug:
            item_slug_name = translit(str(self.name), 'ru', reversed=True)
            self.item_slug = slugify(item_slug_name)
            print(f'name = {self.name} item_slug= {self.item_slug}')

        if self.category and not self.slug_name or self.slug_name != self.category.name:
            self.slug_name = slugify(self.category.slug_name)

        super().save(*args, **kwargs)

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано', blank=True, null=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

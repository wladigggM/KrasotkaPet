from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug_name = models.CharField(max_length=100, default='slug_name')

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug_name = models.CharField(max_length=100, default='slug_name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.category:
            self.category = Category.objects.get(name='Домашняя одежда')
        super().save(*args, **kwargs)


class Reviews(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    comment = models.TextField(max_length=255)
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True, verbose_name='Фотографии')
    last_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

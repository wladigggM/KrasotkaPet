# Generated by Django 4.2.7 on 2024-03-23 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='review',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Оставлен отзыв'),
        ),
    ]

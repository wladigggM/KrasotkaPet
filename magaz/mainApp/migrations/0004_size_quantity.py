# Generated by Django 4.2.7 on 2024-03-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_item_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество'),
        ),
    ]

# Generated by Django 4.2.7 on 2024-03-16 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]

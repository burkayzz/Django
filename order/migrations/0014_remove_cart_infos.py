# Generated by Django 5.0.4 on 2024-05-15 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_cart_infos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='infos',
        ),
    ]

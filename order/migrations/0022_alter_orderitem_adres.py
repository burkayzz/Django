# Generated by Django 5.0.4 on 2024-05-17 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_rename_adresbilgileri_orderitem_adres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='adres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.adres'),
        ),
    ]

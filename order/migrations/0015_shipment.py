# Generated by Django 5.0.4 on 2024-05-16 11:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_remove_cart_infos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cargoNumber', models.CharField(max_length=15, verbose_name='Kargo No')),
                ('status', models.CharField(choices=[('kargoya verildi', 'Kargoya verildi'), ('dağıtıma çıktı', 'Dağıtıma çıktı'), ('Teslim edildi', 'Teslim edildi')], default='Kargoya verildi', max_length=20)),
                ('adres', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.adres')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
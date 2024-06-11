# Generated by Django 5.0.4 on 2024-05-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_remove_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('bekliyor', 'Bekliyor'), ('sipariş oluşturuldu', 'Sipariş Oluşturuldu'), ('iptal edildi', 'İptal Edildi')], default='bekliyor', max_length=20),
        ),
    ]

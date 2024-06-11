# Generated by Django 5.0.4 on 2024-05-10 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalog.brand', verbose_name='Marka'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalog.category', verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_images/', verbose_name='Görsel'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productName',
            field=models.CharField(max_length=150, verbose_name='Ürün ismi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unitPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Fiyat'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unitsInStock',
            field=models.IntegerField(default=0, verbose_name='Stok Adeti'),
        ),
    ]

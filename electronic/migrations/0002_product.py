# Generated by Django 5.0 on 2023-12-19 11:44

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('image', models.ImageField(upload_to='product_image/img')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('condition', models.CharField(choices=[('NEW', 'NEW'), ('OLD', 'OLD')], max_length=200)),
                ('information', models.TextField()),
                ('description', models.TextField()),
                ('stock', models.CharField(choices=[('IN STOCK', 'IN STOCK'), ('OUT OF STOCK', 'OUT OF STOCK')], max_length=200)),
                ('status', models.CharField(choices=[('PUBLISH', 'PUBLISH'), ('DRAFT', 'DRAFT')], max_length=200)),
                ('created_date', models.DateTimeField(default=datetime.timezone)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.brand')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.categorie')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.color')),
                ('filter_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.filter_price')),
            ],
        ),
    ]

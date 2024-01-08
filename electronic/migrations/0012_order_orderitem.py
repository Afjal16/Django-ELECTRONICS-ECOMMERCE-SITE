# Generated by Django 4.2.6 on 2023-12-22 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('electronic', '0011_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postcode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('additional_info', models.TextField()),
                ('amount', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='orderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='product_image/Order_img')),
                ('quantity', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('total', models.CharField(max_length=1000)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.order')),
            ],
        ),
    ]
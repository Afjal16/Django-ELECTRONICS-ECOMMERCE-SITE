# Generated by Django 4.2.6 on 2023-12-19 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0004_alter_product_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=datetime.timezone),
        ),
    ]

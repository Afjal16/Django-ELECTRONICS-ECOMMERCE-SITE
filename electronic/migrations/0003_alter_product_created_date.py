# Generated by Django 5.0 on 2023-12-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-12-22 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0013_order_payment_id_alter_order_date_alter_order_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
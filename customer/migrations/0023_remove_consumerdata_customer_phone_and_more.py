# Generated by Django 5.0.1 on 2024-09-16 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0022_consumerdata_customer_phone_consumerdata_rider_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumerdata',
            name='customer_phone',
        ),
        migrations.RemoveField(
            model_name='consumerdata',
            name='rider_phone',
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0007_alter_orderdetails_order_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='customer_location',
            field=models.CharField(default=None, max_length=255),
        ),
    ]

# Generated by Django 5.0.1 on 2024-09-10 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_users_cart_location_users_cart_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeorder',
            name='item_image',
        ),
    ]

# Generated by Django 5.0.1 on 2024-09-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0027_alter_users_cart_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_cart',
            name='phone_number',
            field=models.CharField(default='0300*******', max_length=20, null=True),
        ),
    ]

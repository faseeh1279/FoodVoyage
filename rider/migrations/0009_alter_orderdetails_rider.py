# Generated by Django 5.1.1 on 2024-10-13 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0008_remove_orderdetails_customer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='rider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rider.rider'),
        ),
    ]

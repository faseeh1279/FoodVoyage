# Generated by Django 5.0.1 on 2024-09-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_alter_register_partner_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_partner',
            name='restaurant_location',
            field=models.CharField(default='restaurant_location', max_length=150),
        ),
    ]

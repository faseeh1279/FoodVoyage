# Generated by Django 5.0.1 on 2024-08-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_register_partner_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_partner',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]

# Generated by Django 5.0.1 on 2024-08-26 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_partner',
            name='username',
        ),
    ]

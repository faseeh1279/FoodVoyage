# Generated by Django 5.0.1 on 2024-08-27 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_register_partner_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_partner',
            name='email',
            field=models.CharField(default='google@example.com', max_length=50),
        ),
    ]

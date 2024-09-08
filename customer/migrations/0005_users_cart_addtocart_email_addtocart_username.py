# Generated by Django 5.0.1 on 2024-09-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_remove_addtocart_customer_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(default='google@example.com', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='addtocart',
            name='email',
            field=models.CharField(default='google@example.com', max_length=50),
        ),
        migrations.AddField(
            model_name='addtocart',
            name='username',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]

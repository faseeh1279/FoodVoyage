from django.db import models

# Create your models here.


class Customer(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    
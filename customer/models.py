from django.db import models

# Create your models here.


class Customer(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    
class AddToCart(models.Model): 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None, null = False)
    item_image = models.ImageField(upload_to="AddToCart")
    item_name = models.CharField(max_length=100)
    item_price = models.CharField(max_length=100) 
from django.db import models

# Create your models here.


class Users_Cart(models.Model): 
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50, default="google@example.com")
    
    

class AddToCart(models.Model): 
    item_image = models.ImageField(upload_to="AddToCart")
    item_name = models.CharField(max_length=100)
    item_price = models.CharField(max_length=100) 
    email = models.CharField(max_length=50, default="google@example.com")
    username = models.CharField(max_length=50, default="", unique=True)
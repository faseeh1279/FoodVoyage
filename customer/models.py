from django.db import models

# Create your models here.


class Users_Cart(models.Model): 
    username = models.CharField(max_length=100, default=None)
    email = models.CharField(max_length=50, default="google@example.com")

    def __str__(self): 
        return self.username 
    

class AddToCart(models.Model): 
    users_cart = models.ForeignKey(Users_Cart, on_delete=models.CASCADE, default=1)
    item_image = models.ImageField(upload_to="AddToCart")
    item_name = models.CharField(max_length=100)
    item_price = models.CharField(max_length=100) 
    def __str__(self): 
        return f"{self.item_name} - {self.users_cart.username}"
    
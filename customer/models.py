from django.db import models

# Create your models here.


class Users_Cart(models.Model): 
    username = models.CharField(max_length=100, default=None)
    email = models.CharField(max_length=50, default="google@example.com")
    phone_number = models.CharField(max_length=20, default="0300*******")
    location = models.CharField(max_length=200, default="Location")
    

    def __str__(self): 
        return self.username 
    

class AddToCart(models.Model): 
    users_cart = models.ForeignKey(Users_Cart, on_delete=models.CASCADE, default=1)
    item_image = models.ImageField(upload_to="AddToCart")
    item_name = models.CharField(max_length=100)
    item_price = models.CharField(max_length=100) 
    restaurant_name = models.CharField(max_length=100, default="restaurant_name") 
    def __str__(self): 
        return f"{self.item_name} - {self.users_cart.username}"
    


class PlaceOrder(models.Model): 
    users_cart = models.ForeignKey(Users_Cart, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=100)
    item_price = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=100, default="restaurant_name")
    order_status = models.CharField(max_length=100, default="pending")
    customer_name = models.CharField(max_length=100, default=None)
    total_amount = models.CharField(max_length=100)
    customer_location = models.CharField(max_length=100)
    current_datetime = models.CharField(max_length=100, default="datetime")
    def __str__(self): 
        return f"{self.customer_name} ordered at location {self.customer_location} for amount {self.total_amount}"

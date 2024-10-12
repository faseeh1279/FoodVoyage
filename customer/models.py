from django.db import models

# Create your models here.


class Users_Cart(models.Model): 
    username = models.CharField(max_length=100, default=None)
    email = models.CharField(max_length=50, default="google@example.com")
    phone_number = models.CharField(max_length=20, default="0300*******", null=True)
    location = models.CharField(max_length=300, default="Location")
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
    customer_location = models.CharField(max_length=300)
    current_datetime = models.CharField(max_length=100, default="datetime")
    def __str__(self): 
        return f"{self.customer_name} ordered at location {self.customer_location} for amount {self.total_amount} Order Status : {self.order_status}"


class ConsumerData(models.Model): 
    customer_name = models.ForeignKey(Users_Cart, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    time_stamp = models.CharField(max_length=155)
    customer_id = models.CharField(max_length=155)
    customer_location = models.CharField(max_length=255)
    rider = models.CharField(max_length=155)
    def __str__(self): 
        return f"{self.customer_name} {self.message} at {self.customer_location} by {self.rider}"


class OrderHistory(models.Model): 
    customer_name = models.CharField(max_length=255)
    customer_location = models.CharField(max_length=255) 
    item_name = models.CharField(max_length=255)
    item_price = models.CharField(max_length=255)
    total_price = models.CharField(max_length=255)
    timestamp = models.CharField(max_length=155)
    def __str__(self): 
        return f"Customer - {self.customer_name} at location: {self.customer_location} on {self.timestamp}"




    
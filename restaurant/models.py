from django.db import models
import customer.models 


# Create your models here.
class Register_Partner(models.Model): 
    restaurant_name = models.CharField(max_length=30)
    restaurant_slogan = models.CharField(max_length=100)
    restaurant_description = models.TextField(default="Restaurant Description")
    restaurant_image = models.ImageField(upload_to='restaurant_profile_image')
    email = models.CharField(max_length=50, default="google@example.com")
    username = models.CharField(max_length=50, default="", unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    restaurant_location = models.CharField(max_length=150, default="restaurant_location")

    def __str__(self): 
        return self.restaurant_name  # or self.email
    
    
class AddFood(models.Model):
    restaurant = models.ForeignKey(Register_Partner, on_delete=models.CASCADE)  # Link to the partner
    item_name = models.CharField(max_length=50)
    item_description = models.TextField(default="Food Item Description")
    item_image = models.ImageField(upload_to="Add-Food-Items-Images")
    item_price = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.item_name

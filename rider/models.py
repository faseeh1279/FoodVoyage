from django.db import models

# Create your models here.

class Rider(models.Model): 
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, default="google@example.com", unique=True)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    bio = models.TextField(default="Rider's Bio")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to="RiderProfileImage")
    vehicle_type = models.CharField(max_length=50)
    def __str__(self): 
        return self.name  

class OrderDetails(models.Model): 
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='pending_orders')
    customer_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    order_status = models.BooleanField(default=False) # False means that order is pending and True means that order has been delivered. 
    rider_name = models.CharField(max_length=100, default="rider_name")
    




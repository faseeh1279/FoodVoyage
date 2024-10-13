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
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_location = models.CharField(max_length=255, default=None)
    wallet = models.IntegerField(default=0)
    order_completed = models.IntegerField(default = 0)
    def __str__(self): 
        return f'Rider : {self.rider} Wallet: {self.wallet} Orders Completed{self.order_completed}'
    
    




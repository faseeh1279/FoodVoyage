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

from django.contrib import admin
from . import models 
# Register your models here.

admin.site.register(models.AddToCart)
admin.site.register(models.Users_Cart)
admin.site.register(models.PlaceOrder)
admin.site.register(models.ConsumerData)


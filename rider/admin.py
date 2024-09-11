from django.contrib import admin
from . import models 
# Register your models here.

admin.site.register(models.OrderDetails)
admin.site.register(models.Rider)

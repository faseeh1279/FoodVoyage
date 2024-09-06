from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.index, name='home'),
    path("notification/", views.notification, name="notification"),
    path("customer/add-to-cart/", views.add_to_cart, name="add-to-cart"), 
]
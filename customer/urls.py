from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.index, name='home'),
    path('order-now/', views.order_now, name='order'), 
    path("notification/", views.notification, name="notification"),
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"), 
]
from django.urls import path
from . import views 
urlpatterns = [
    path("", views.index, name='rider-home'), 
    path("dashboard/", views.dashboard, name="rider-dashboard"), 
   
    path("deliver-order-to-customer/", views.deliver_order, name="deliver-order-to-customer"), 
    
    path("get-order-details/", views.get_order_details, name="get-order-details"),
    
    path("get-placed-order-details/", views.get_placed_orders_details, name="get-placed-order-details"),
    
    # Get customer Phone Number ONLY
    path("get-customer-phoneNumber/", views.get_customer_phoneNumber, name="get-customer-phoneNumber"), 
    path("get-orders-from-database/", views.get_orders, name="get-orders-from-database"), 
    ]
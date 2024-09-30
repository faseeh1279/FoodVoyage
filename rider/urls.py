from django.urls import path
from . import views 
urlpatterns = [
    path("", views.index, name='rider-home'), 
    path("dashboard/", views.dashboard, name="rider-dashboard"), 
    path("deliver-order-to-customer/", views.deliver_order, name="deliver-order-to-customer"), 
    path("get-order-details/", views.get_order_details, name="get-order-details"),
    # Get customer Phone Number ONLY
    path("get-customer-phoneNumber/", views.get_customer_phoneNumber, name="get-customer-phoneNumber"), 
    path("get-orders-from-database/", views.get_orders, name="get-orders-from-database"), 
    path("get-rider-name/", views.get_rider_name, name="get-rider-name"), 
    path("upload-consumer-data/", views.upload_consumer_data, name="upload_consumer_data"),
    path("successfully-delivered-order/", views.successfully_delivered_order, name="successfully-delivered-order"),     ]
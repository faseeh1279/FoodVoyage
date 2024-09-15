from django.urls import path
from . import views 
urlpatterns = [
    path("", views.index, name='rider-home'), 
    path("dashboard/", views.dashboard, name="rider-dashboard"), 
    path("get-rider-name/", views.rider_name, name="get-rider-name"),
    path("deliver-order-to-customer/", views.deliver_order, name="deliver-order-to-customer"), 
    path("order-details/", views.order_details, name="order-details"), 
    path("get-order-details/", views.get_order_details, name="get-order-details"),
    path("check-placed-orders/", views.check_placed_orders, name="check-placed-orders"),
    path("get-placed-order-details/", views.get_placed_orders_details, name="get-placed-order-details") 
    
]
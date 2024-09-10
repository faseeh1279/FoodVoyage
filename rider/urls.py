from django.urls import path
from . import views 
urlpatterns = [
    path("", views.index, name='rider-home'), 
    path("dashboard/", views.dashboard, name="rider-dashboard"), 
    path("get-rider-name/", views.rider_name, name="get-rider-name"),
    path("deliver-order-to-customer", views.deliver_order, name="deliver-order-to-customer"), 
    path("order-details/", views.order_details, name="order-details"), 
]
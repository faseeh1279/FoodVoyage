from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.index, name='home'),
    path("view-cart/", views.view_cart, name="view-cart"),
    path('order-now/', views.order_now, name='order'), 
    path("notification/", views.notification, name="notification"),
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"), 
    path("get-data/", views.get_data, name="get-data"), 
    path("delete-data/", views.delete_data, name="delete-data"), 
    path("get-cart-details/", views.get_cart_details, name="get-cart-details"), 
    path("cart/", views.cart, name='simple-cart'), 
    path("place-order/", views.place_order, name="place-order"),
    path("place-order-details/", views.place_order_details, name="place-order-details"), 
    path("place-order-credentials/", views.place_order_credentials, name="place-order-credentials"),  
]
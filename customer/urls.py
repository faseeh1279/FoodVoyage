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
]
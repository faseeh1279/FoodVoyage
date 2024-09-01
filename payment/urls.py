from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.purchase, name="checkout"),
    path('/success/', views.success, name="success")
]
from django.urls import path 
from . import views 
urlpatterns = [
    path("", views.home, name="restaurant-home"), 
    path("dashboard/", views.dashboard, name="restaurant-dashboard"), 
]
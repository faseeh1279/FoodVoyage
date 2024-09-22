from django.urls import path 
from . import views 
urlpatterns = [
    path("", views.home, name="restaurant-home"),
    path("dashboard/", views.dashboard, name="restaurant-dashboard"),
    path("dashboard/addfood/", views.add_food, name="restaurant-add-food"),
    path("delete-item/<int:id>", views.delete_item, name="delete-item"), 
    path("update-item/<int:id>", views.update_item, name="update-food-item"), 
    path("populate-dashboard/", views.populate_dashboard, name="populate-dashboard"),
]

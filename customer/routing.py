from django.urls import path 
from . import consumers 

websocket_urlpatterns = [
    path("ws/sc/customer/",consumers.MySyncConsumer.as_asgi()), 
]
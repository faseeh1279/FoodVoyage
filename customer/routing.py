from django.urls import path 
from . import consumers 

websocket_urlpatterns = [
    path("ws/sc/place_order/",consumers.MySyncConsumer.as_asgi()), 
]
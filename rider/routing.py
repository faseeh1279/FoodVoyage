from django.urls import path 
from . import consumers 

websocket_urlpatterns = [
    path('ws/sc/rider/', consumers.MySyncConsumer.as_asgi()),
]
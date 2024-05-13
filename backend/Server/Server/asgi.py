import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from myapp.consumers import TestConsumer

ws_patterns = [
    path('ws/test/', TestConsumer)
]
application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})
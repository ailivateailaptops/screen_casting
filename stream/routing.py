from django.urls import re_path
from stream.consumers import ScreenShareConsumer

websocket_urlpatterns = [
    re_path(r'ws/screen/', ScreenShareConsumer.as_asgi()),
]

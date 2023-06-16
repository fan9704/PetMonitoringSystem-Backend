from django.urls import re_path

from api.consumers import NotifyConsumer

websocket_urlpatterns = [
    re_path(r'ws/notify/<str:username>/', NotifyConsumer.as_asgi()),
]
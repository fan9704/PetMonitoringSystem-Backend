"""
ASGI config for PetMonitoringSystemBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

import django
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PetMonitoringSystemBackend.settings')
django.setup()
from api.routing import websocket_urlpatterns  # must put later than set up

application = ProtocolTypeRouter({
    # http
    "http": get_asgi_application(),
    # websocket
    "websocket":
    # AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    # ),
})

"""
ASGI config for PetMonitoringSystemBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from ws import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PetMonitoringSystemBackend.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    # http请求使用这个
    "http": get_asgi_application(),

    # websocket请求使用这个
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})




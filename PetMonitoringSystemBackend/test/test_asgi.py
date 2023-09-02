from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.test import TestCase, override_settings

from api.routing import websocket_urlpatterns


class TestASGIConfig(TestCase):
    @override_settings(ASGI_APPLICATION='PetMonitoringSystemBackend.asgi.application')
    def test_asgi_application(self):
        asgi_application = get_asgi_application()

        self.assertIsNotNone(asgi_application)

    def test_websocket_routing(self):
        application = ProtocolTypeRouter({
            "websocket": URLRouter(
                websocket_urlpatterns
            ),
        })

        self.assertIsNotNone(application)

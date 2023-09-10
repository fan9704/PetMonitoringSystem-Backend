import os
import unittest
from django.core.wsgi import get_wsgi_application


class WSGITestCase(unittest.TestCase):
    def test_wsgi_application_variable(self):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'PetMonitoringSystemBackend.settings'

        wsgi_application = get_wsgi_application()

        self.assertIsNotNone(wsgi_application)

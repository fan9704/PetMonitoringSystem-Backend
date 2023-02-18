"""
WSGI config for PetMonitoringSystemBackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django_forest import init_forest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PetMonitoringSystemBackend.settings')
init_forest()
application = get_wsgi_application()

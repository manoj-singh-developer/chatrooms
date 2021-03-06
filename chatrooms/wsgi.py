"""
WSGI config for notaso project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

ENVIRONMENT = os.getenv('ENVIRONMENT', 'DEVELOPMENT').title()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatrooms.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', ENVIRONMENT)

from dj_static import Cling
from configurations.wsgi import get_wsgi_application
from django.conf import settings
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer

_django_app = Cling(get_wsgi_application())
_websocket_app = uWSGIWebsocketServer()


def application(environ, start_response):
    if environ.get('PATH_INFO').startswith(settings.WEBSOCKET_URL):
        return _websocket_app(environ, start_response)
    return _django_app(environ, start_response)

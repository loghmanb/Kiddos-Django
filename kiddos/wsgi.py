"""
WSGI config for kiddos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from . import load_custom_environment_variables

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kiddos.settings')

load_custom_environment_variables()

application = get_wsgi_application()

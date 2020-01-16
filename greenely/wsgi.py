"""
WSGI config for greenely project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from greenely.project_environment import PROJECT_ENV
from greenely.default_values import (PRODUCTION_ENVIRONMENT,
                                     DEVELOPMENT_ENVIRONMENT)

from django.core.wsgi import get_wsgi_application

if PROJECT_ENV == PRODUCTION_ENVIRONMENT:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'greenely.settings.production_settings')
elif PROJECT_ENV == DEVELOPMENT_ENVIRONMENT:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'greenely.settings.development_settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'greenely.settings.local_settings')

application = get_wsgi_application()

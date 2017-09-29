"""
WSGI config for quizsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quizsite.settings")

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())
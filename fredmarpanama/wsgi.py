"""
WSGI config for fredmarpanama project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fredmarpanama.settings")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)

# placeholder="eg: /home/jorgged/.virtualenvs/my-webapp-virtualenv
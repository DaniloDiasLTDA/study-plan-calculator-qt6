import os

from django.core.asgi import get_asgi_application

from danilodias.settings import APP_SETTINGS_PAT

os.environ.setdefault('DJANGO_SETTINGS_MODULE', APP_SETTINGS_PAT)

application = get_asgi_application()

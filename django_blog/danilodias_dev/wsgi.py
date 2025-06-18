import os

from danilodias.settings import APP_SETTINGS_PATH
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', APP_SETTINGS_PATH)

application = get_wsgi_application()

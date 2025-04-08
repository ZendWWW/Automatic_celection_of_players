import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Automatic_celection_of_players.settings')

application = get_wsgi_application()

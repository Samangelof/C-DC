from django.apps import AppConfig
from django.conf import settings
import os

class AuthsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auths'

    def ready(self):
        media_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')
        if not os.path.exists(media_path):
            os.makedirs(media_path)


        settings.MEDIA_ROOT = media_path
        settings.MEDIA_URL = '/media/'
"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: utils
import os

# IMPORT: django
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_kwalk.settings")
application = get_asgi_application()

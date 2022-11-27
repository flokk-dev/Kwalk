"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: django
from django.contrib import admin
from django.urls import path, include

# IMPORT: rest
from rest_framework import routers

# IMPORT: project
from api_kwalk.urls import router as player_router
from api_auth.urls import get_auth_urls


# ROUTER
router = routers.DefaultRouter()
router.registry.extend(player_router.registry)


# URL
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    *get_auth_urls(parent="api")
]

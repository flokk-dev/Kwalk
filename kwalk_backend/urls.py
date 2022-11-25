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
from kwalk.urls import router as player_router


# ROUTER
router = routers.DefaultRouter()
router.registry.extend(player_router.registry)


# URL
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]

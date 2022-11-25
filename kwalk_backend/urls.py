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
from user_management.urls import router as user_management_router


# ROUTER
router = routers.DefaultRouter()
router.registry.extend(player_router.registry)
router.registry.extend(user_management_router.registry)


# URL
urlpatterns = [
    path("admin/", admin.site.urls),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("", include(router.urls))
]

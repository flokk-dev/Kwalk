"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: rest
from rest_framework import routers

# IMPORT: project
from .views import MeViewSet


# ROUTER
router = routers.DefaultRouter()
router.register("me", MeViewSet, basename="me")

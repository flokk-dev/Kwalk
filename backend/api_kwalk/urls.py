"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: rest
from rest_framework import routers

# IMPORT: project
from .views import PlayerViewSet, InventoryViewSet, CardViewSet


# ROUTER
router = routers.DefaultRouter()

router.register("player", PlayerViewSet)
router.register("inventory", InventoryViewSet)
router.register("card", CardViewSet)

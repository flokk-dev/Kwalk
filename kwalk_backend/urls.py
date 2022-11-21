"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: django
from django.contrib import admin
from django.urls import path

# IMPORT: project
from kwalk import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("roll/", views.add_cards),
    path("cards/", views.display_cards)
]

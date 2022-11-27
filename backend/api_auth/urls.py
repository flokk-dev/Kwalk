"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: django
from django.urls import path

# IMPORT: rest
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# IMPORT: project
from .views import MyTokenObtainPairView


# URLS
def get_auth_urls(parent="api"):
    return [
        path(f"{parent}/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
        path(f"{parent}/token/refresh/", TokenRefreshView.as_view(), name="token_refresh")
    ]

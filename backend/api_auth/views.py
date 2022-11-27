"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: rest
from rest_framework_simplejwt.views import TokenObtainPairView

# IMPORT: project
from .serializers import MyTokenObtainPairSerializer


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

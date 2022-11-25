"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: django
from django.shortcuts import render
from django.contrib.auth.models import User

# IMPORT: rest
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# IMPORT: project
from user_management.serializers import UserSerializer


# Create your views here.
class MeViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data

        return Response(user_data)

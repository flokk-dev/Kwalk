"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: django
from django.http import HttpResponse
from django.shortcuts import render

# IMPORT: rest
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# IMPORT: project
from .models import Player, Inventory, Card
from .serializers import PlayerSerializer, InventorySerializer, CardSerializer


# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = (IsAuthenticated, )

    filterset_fields = ["date", ]
    search_fields = ["pseudo", ]


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (IsAuthenticated, )


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated, )

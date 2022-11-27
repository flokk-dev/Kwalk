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

# IMPORT: project
from .models import Player, Inventory, Card
from .serializers import PlayerSerializer, InventorySerializer, CardSerializer


# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    filterset_fields = ["date", ]
    search_fields = ["pseudo", ]


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

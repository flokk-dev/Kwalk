"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: django
from rest_framework import serializers

# IMPORT: project
from .models import Player, Inventory, Card


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"

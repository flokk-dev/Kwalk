"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: django
from django.db import models


class Player(models.Model):
    # Attributes
    pseudo = models.fields.CharField(max_length=20, default="pseudo_by_default")
    name = models.fields.CharField(max_length=50, default="name_by_default")
    surname = models.fields.CharField(max_length=50, default="surname_by_default")
    date = models.DateField()

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"


class Folder(models.Model):
    # Attributes
    nb_cards = models.fields.PositiveIntegerField(default=0)

    # Foreign key
    parent = models.ForeignKey("Player", null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Folder"
        verbose_name_plural = "Folders"


class Card(models.Model):
    # Attributes
    name = models.fields.CharField(max_length=20, default="name_by_default")
    desc = models.fields.CharField(max_length=20, default="desc_by_default")
    rarity = models.fields.CharField(max_length=20, default="rarity_by_default")

    # Foreign key
    parent = models.ForeignKey("Folder", null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"

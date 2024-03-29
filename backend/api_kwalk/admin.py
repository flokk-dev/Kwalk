"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: django
from django.contrib import admin

# IMPORT: project
from .models import Player, Inventory, Card


# Register your inlines here.
class InventoryInLine(admin.TabularInline):
    model = Inventory
    extra = 0


class CardInLine(admin.TabularInline):
    model = Card
    extra = 0


# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("id", "pseudo")
    list_filter = ("pseudo", "date")
    search_fields = ("pseudo", )

    inlines = (InventoryInLine, )


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("id", "nb_cards")
    list_filter = ("nb_cards", )

    inlines = (CardInLine, )


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "desc", "rarity")
    list_filter = ("name", "rarity")
    search_fields = ("name", "rarity")

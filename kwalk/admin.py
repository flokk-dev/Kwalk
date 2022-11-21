"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: django
from django.contrib import admin

# IMPORT: project
from .models import Player, Folder, Card


# Register your inlines here.
class FolderInLine(admin.TabularInline):
    model = Folder
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

    inlines = (FolderInLine, )


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("id", "nb_cards")
    list_filter = ("nb_cards", )

    inlines = (CardInLine, )


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", "desc")
    search_fields = ("name", )

"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: django
from django.http import HttpResponse
from django.shortcuts import render

# IMPORT: project
from kwalk.models import Card


# Create your views here.
def add_cards(request):
    return render(request, "listings/roll.html", {"cards": Card.objects.all()})


def display_cards(request):
    return render(request, "listings/cards.html", {"cards": Card.objects.all()})

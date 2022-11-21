"""
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
"""

# IMPORT: django
from django.test import TestCase
from kwalk.models import Player, Folder, Card


# Create your tests here.
class PlayerTestCase(TestCase):
    pass


class FolderTestCase(TestCase):
    pass


class CardTestCase(TestCase):
    def test_create_card(self):
        nb_cards = Card.objects.count()

        new_card = Card()
        new_card.name, new_card.desc, new_card.rarity = "pikachu", "type électrique", "épique"
        new_card.save()

        new_nb_cards = Card.objects.count()
        self.assertTrue(new_nb_cards == nb_cards+1)

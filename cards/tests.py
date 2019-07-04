from django.test import TestCase, SimpleTestCase
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.urls import reverse

class CardsTest(TestCase):

  def test_create_card(self):
    Card = get_card_model()
    card = Card.objects.create_card(
      name='test'
    )
    self.assertEqual(card.name, 'test')
    self.assertTrue(card.name)

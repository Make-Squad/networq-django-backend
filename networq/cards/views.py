from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Card

def card(request, card_id):
    """
    This page will render user feed template. 
    """
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cards/businesscard.html', {
        'card': card
    })

def cards(request):
    """
    This page will render all users.
    """
    all_cards = get_list_or_404(Card,)
    return render(request, 'cards/cards.html', {
        'cards': all_cards
    })


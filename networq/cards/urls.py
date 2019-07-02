from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # SHOW one card 
    path('<int:card_id>', views.card, name='card'),
    
    # SHOW all cards
    path('', views.cards, name='cards'),
    ]
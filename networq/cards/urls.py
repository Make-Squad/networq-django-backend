from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # cards index page; aka user's feed
    url('cards', views.cards, name='cards')
    ]
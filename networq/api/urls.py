from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # /users/settings - edit user settings 

    # SHOW all users
    url('users', views.UserList.as_view(), name='users_list'),

    # SHOW one user's dashboard/profile page 
    path('users/<username>', views.UserDetail.as_view(), name='user_detail'),
    
    # # SHOW all cards
    url('cards', views.CardList.as_view(), name='cards_list'),

    # SHOW one card's dashboard/profile page 
    url('cards/<card_id>', views.CardDetail.as_view(), name='card_detail'),
    
    ]
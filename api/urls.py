from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    # /users/settings - edit user settings 

    # SHOW one user as DetailView
    path('users/<username>', views.UserDetail.as_view(), name='user_detail'),

    # SHOW all users as ListView 
    url('users', views.UserList.as_view(), name='users_list'),

    # SHOW one card as DetailView
    path('cards/<int:card_id>', views.CardDetail.as_view(), name='card_detail'),
    
    # # SHOW all cards as ListView
    url('cards', views.CardList.as_view(), name='cards_list'),


    ]

from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # /users/settings - edit user settings 

    # SHOW one user's dashboard/profile page 
    path('users/<username>', views.user, name='user'),
    
    # SHOW all users
    url('users', views.users, name='users'),

    # root 
    url(r'', views.index, name='index')
    ]
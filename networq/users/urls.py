from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # /users/settings - edit user settings 
    
    # user's dashboard/profile page 
    url('users/', views.users, name='users'),
    url(r'', views.index, name='index')
    ]
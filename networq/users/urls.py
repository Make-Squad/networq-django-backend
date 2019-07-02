from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # /users/settings - edit user settings 

    # SHOW all users
    url('users', views.UserList.as_view(), name='users_list'),

    # SHOW one user's dashboard/profile page 
    url('user/<username>', views.UserDetail.as_view(), name='user_detail'),
    
    # root 
    url(r'', views.index, name='index')
    ]
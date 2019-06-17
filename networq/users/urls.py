from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url('users/', views.users, name='users'),
    url(r'', views.index, name='index')
    ]
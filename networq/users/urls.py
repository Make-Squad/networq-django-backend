from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # /users/settings - edit user settings 
    
    # user's dashboard/profile page 
    url('user/<username>', views.user, name='user'),
    # path('<int:question_id>/vote/', views.user, name='vote'),
    url(r'', views.index, name='index')
    ]
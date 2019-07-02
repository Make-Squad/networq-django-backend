from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import User

def index(request):
    """
    This page will render the index template. 

    For now, lets render all cards and all users here. 
    """
    return render(request, 'users/index.html')

def users(request):
    """
    This page will render all users.
    """
    active_users = get_list_or_404(User, is_active=True)
    return render(request, 'users/users.html', {
        'users': active_users
    })

def user(request, username):
    """
    This page will render user feed template. 
    """
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {
        'user': user
    })
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls import reverse_lazy 
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login


from .models import User

def index(request):
    """
    This page will render the index template. 

    For now, lets render all cards and all users here. 
    """
    return render(request, 'users/index.html')

def user(request, username):
    """
    This page will render user feed template. 
    """
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {
        'user': user
    })

def users(request):
    """
    This page will render all users.
    """
    active_users = get_list_or_404(User, is_active=True)
    return render(request, 'users/users.html', {
        'users': active_users
    })

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None: 
        # redirect to user dashboard
        return

# class UserCreate(CreateView):
#     model = User
#     fields = '__all__'

# class UserUpdate(UpdateView):
#     model = User
#     fields = '__all__'

# class UserDelete(DeleteView):
#     model = User
#     success_url = reverse_lazy('user_dashboard')

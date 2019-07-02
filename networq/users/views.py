from django.http import HttpResponse

def index(request):
    """
    This page will render the index template. 

    For now, lets render all cards and all users here. 
    """
    return HttpResponse("This is the root.")

def user(request, username):
    """
    This page will render user feed template. 
    """
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {
        'user': user
    })
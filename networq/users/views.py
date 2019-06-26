from django.http import HttpResponse

def index(request):
    """
    This page will render the index template. 
    """
    return HttpResponse("This is the root.")

def users(request, user_id):
    """
    This page will render user feed template. 
    """
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/profile.html', {
        'user': user
    })
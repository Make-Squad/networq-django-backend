from django.http import HttpResponse

def index(request):
    """
    This page will render the index template. 
    """
    return HttpResponse("This is the root.")

def users(request):
    """
    This page will render user feed template. 
    """
    return HttpResponse("This is the user's profile page.")
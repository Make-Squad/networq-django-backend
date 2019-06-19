from django.http import HttpResponse

def cards(request):
    """
    This page will render the cards template. 
    """
    return HttpResponse("This is where you will see cards.")

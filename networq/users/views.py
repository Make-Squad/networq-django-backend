from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializer

def index(request):
    """
    This page will render the index template. 

    For now, lets render all cards and all users here. 
    """
    return HttpResponse("This is the root.")

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()[:20]
        data = UserSerializer(users, many=True).data
        return Response(data)

class UserDetail(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        data = UserSerializer(user).data
        return Response(data)
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from users.models import User
from cards.models import Card
from .serializers import UserSerializer , CardSerializer

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()[:20]
        data = UserSerializer(users, many=True).data
        return Response(data)

class UserDetail(APIView):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        data = UserSerializer(user).data
        return Response(data)

class CardList(APIView):
    def get(self, request):
        cards = Card.objects.all()[:20]
        data = CardSerializer(cards, many=True).data
        return Response(data)

class CardDetail(APIView):
    def get(self, request, card_id):
        card = get_object_or_404(Card, pk=card_id)
        data = CardSerializer(card).data
        return Response(data)
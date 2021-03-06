from rest_framework import serializers

from users.models import User
from cards.models import Card

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Card
        fields = '__all__'
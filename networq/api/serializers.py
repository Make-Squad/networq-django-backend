from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# class CardSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = Card
#         field = '__all__'
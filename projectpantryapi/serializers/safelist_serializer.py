from rest_framework import serializers
from django.contrib.auth.models import User
from projectpantryapi.models import SafeList
from projectpantryapi.models.food import Food

class ListOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        
class SafeFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'location', 'quantity', 'tags')
        depth = 1

class SafeListSerializer(serializers.ModelSerializer):

    safe_food = SafeFoodSerializer()
    list_owner = ListOwnerSerializer()

    class Meta:
        model = SafeList
        fields = ('id', 'list_owner', 'safe_food')
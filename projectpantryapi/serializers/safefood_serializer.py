from rest_framework import serializers
from django.contrib.auth.models import User
from projectpantryapi.models import SafeFood, Food

class ListOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class SafeListFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'location', 'quantity', 'tags')
        depth = 1

class SafeFoodSerializer(serializers.ModelSerializer):

    list_owner = ListOwnerSerializer()
    food = SafeListFoodSerializer()

    class Meta:
        model = SafeFood
        fields = ('id', 'list_owner', 'food')

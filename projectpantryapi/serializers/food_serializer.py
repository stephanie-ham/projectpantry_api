from rest_framework import serializers
from django.contrib.auth.models import User
from projectpantryapi.models import Food, SafeFood
from projectpantryapi.models.quantity import Quantity


class FoodUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class SafeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SafeFood
        fields = ['id']

class FoodSerializer(serializers.ModelSerializer):
    user = FoodUserSerializer()
    safe_foods = SafeSerializer(many=True)

    class Meta:
        model = Food
        fields = ('id', 'name', 'location', 'quantity', 'user', 'tags', 'safe_foods')
        depth = 1

class FilterByQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ('id', 'title')

class CreateFoodSerializer(serializers.Serializer):
    name = serializers.CharField()
    locationId = serializers.IntegerField()
    quantityId = serializers.IntegerField()

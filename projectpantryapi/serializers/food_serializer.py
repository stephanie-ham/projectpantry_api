from rest_framework import serializers
from django.contrib.auth.models import User
from projectpantryapi.models import Food, Location, Quantity

class FoodUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['title']

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ['title']

class FoodSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    quantity = QuantitySerializer()
    user = FoodUserSerializer()

    class Meta:
        model = Food
        fields = ('id', 'name', 'location', 'quantity', 'user')
        depth = 1

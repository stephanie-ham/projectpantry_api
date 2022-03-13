from rest_framework import serializers
from django.contrib.auth.models import User
from projectpantryapi.models import Food


class FoodUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class FoodSerializer(serializers.ModelSerializer):
    # location = LocationSerializer()
    # quantity = QuantitySerializer()
    user = FoodUserSerializer()
    # tags = FoodTagSerializer(many=True)

    class Meta:
        model = Food
        fields = ('id', 'name', 'location', 'quantity', 'user', 'tags')
        depth = 1

class CreateFoodSerializer(serializers.Serializer):
    name = serializers.CharField()
    locationId = serializers.IntegerField()
    quantityId = serializers.IntegerField()

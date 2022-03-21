from rest_framework import serializers
from django.contrib.auth.models import User
from projectpantryapi.models import Food, Location, Quantity, SafeFood, Tag 


class FoodUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        
class FoodTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'label')
        
class FoodLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'title')
        
class FoodQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ('id', 'title')

class SafeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SafeFood
        fields = ['id']

class FoodSerializer(serializers.ModelSerializer):
    user = FoodUserSerializer()
    location = FoodLocationSerializer()
    quantity = FoodQuantitySerializer()
    safe_foods = SafeSerializer(many=True)
    tags = FoodTagSerializer(many=True)
    
    class Meta:
        model = Food
        fields = ('id', 'name', 'location', 'quantity', 'user', 'tags', 'safe_foods', 'is_safe')
        depth = 1


class CreateFoodSerializer(serializers.Serializer):

    name = serializers.CharField()
    locationId = serializers.IntegerField()
    quantityId = serializers.IntegerField()
    # tags = serializers.DjangoModelField(model=Tag)

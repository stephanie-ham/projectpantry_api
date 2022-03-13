from rest_framework import serializers
from django.contrib.auth.models import User
from projectpantryapi.models import Food


class FoodUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = ['title']

# class QuantitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quantity
#         fields = ['title']
# class TagSerializer(serializers.ModelSerializer):
#     model = Tag
#     fields = ['label']

# class FoodTagSerializer(serializers.ModelSerializer):
#     tag = TagSerializer()
#     class Meta:
#         model = FoodTag
#         fields = ['tag']

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
    location = serializers.IntegerField()
    quantity = serializers.IntegerField()

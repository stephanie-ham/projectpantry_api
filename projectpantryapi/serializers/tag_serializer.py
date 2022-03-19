from rest_framework import serializers
from django.contrib.auth.models import User
from projectpantryapi.models import Tag
from projectpantryapi.models.food_tag import FoodTag


class TagUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class TagSerializer(serializers.ModelSerializer):
    created_by = TagUserSerializer()

    class Meta:
        model = Tag
        fields = ('id', 'label', 'created_by')
        depth = 1

class FoodTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodTag
        fields = ('id', 'tag', 'food')
        depth = 1

class CreateTagSerializer(serializers.Serializer):
    label = serializers.CharField()

class AddTagToFoodSerializer(serializers.Serializer):
    tag = serializers.IntegerField()
    food = serializers.IntegerField()

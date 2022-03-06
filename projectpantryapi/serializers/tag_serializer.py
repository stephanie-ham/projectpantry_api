from rest_framework import serializers
from django.contrib.auth.models import User
from projectpantryapi.models import Tag


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
        
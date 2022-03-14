from rest_framework import serializers
from projectpantryapi.models import Quantity

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ('id', 'title')
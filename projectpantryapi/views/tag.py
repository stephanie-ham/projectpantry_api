from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from projectpantryapi.models import Tag

class TagView(ViewSet):
    
    def retrieve(self, request):
        tags = Tag.objects.all()
        
        serializer = TagSerializer()
        return Response(serializer.data)
    
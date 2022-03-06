from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projectpantryapi.models import Tag
from projectpantryapi.serializers import TagSerializer

class TagView(ViewSet):
    @swagger_auto_schema(responses={
        200: openapi.Response(
            description="The list of tags",
            schema=TagSerializer(many=True)
        )
    })
    def list(self, request):
        """Get a list of tags"""
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
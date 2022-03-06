from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projectpantryapi.models import Tag
from projectpantryapi.serializers import TagSerializer

class TagView(ViewSet):

    @swagger_auto_schema(responses={
        200: openapi.Response(
            description="The list of tags created by current user",
            schema=TagSerializer(many=True)
        )
    })
    def list(self, request):
        """Get a list of tags for the current user"""
        tags = Tag.objects.filter(created_by=request.auth.user)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

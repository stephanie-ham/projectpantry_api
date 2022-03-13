from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projectpantryapi.models import Tag
from projectpantryapi.serializers import CreateTagSerializer, MessageSerializer,TagSerializer

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

    @swagger_auto_schema(
        request_body=CreateTagSerializer,
        responses={
            201: openapi.Response(
                description="Returns the created tag",
                schema=TagSerializer()
            ),
            400: openapi.Response(
                description="Validation Error",
                schema=MessageSerializer()
            )
        }
    )
    def create(self, request):
        """Create a tag for the current user"""
        try:
            tag = Tag.objects.create(
                created_by=request.auth.user,
                label=request.data['label']
            )
            serializer = TagSerializer(tag)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            204: openapi.Response(
                description="No content, tag deleted successfully",
            ),
            404: openapi.Response(
                description="Tag not found",
                schema=MessageSerializer()
            )
        }
    )
    @action(methods=['delete'], detail=True)
    def delete(self, request, pk):
        """Delete a tag"""
        try:
            tag = Tag.objects.get(pk=pk, created_by=request.auth.user)
            tag.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


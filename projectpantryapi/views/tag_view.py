from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projectpantryapi.models import Food, Tag
from projectpantryapi.models.food_tag import FoodTag
from projectpantryapi.serializers import ( AddTagToFoodSerializer,
    CreateTagSerializer, FoodTagSerializer, MessageSerializer, TagSerializer )

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


    @swagger_auto_schema(
        request_body=CreateTagSerializer(),
        responses={
            204: openapi.Response(
                description="No Content, Tag updated successfully"
            )
        }
    )
    def update(self, request, pk=None):
        """Update a tag"""
        tag = Tag.objects.get(pk=pk, created_by=request.auth.user)
        tag.label = request.data["label"]

        tag.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    # @swagger_auto_schema(
    #     method='POST',
    #     request_body=AddTagToFoodSerializer(),
    #     responses={
    #         201: openapi.Response(
    #             description="Returns message that tag was added to food",
    #             schema=FoodTagSerializer()
    #         ),
    #         404: openapi.Response(
    #             description="Product not found",
    #             schema=MessageSerializer()
    #         ),
    #     }
    # )
    @swagger_auto_schema(
        method='POST',
        request_body=AddTagToFoodSerializer(),
        responses={
            201: openapi.Response(
                description="Returns message that tag was added to food"
            ),
            404: openapi.Response(
                description="Tag not found",
                schema=MessageSerializer()
            ),
        }
    )
    @action(methods=['post'], detail=True)
    def add_to_food(self, request, pk=None):
        """Add a tag to a current user's food"""
        try:

            tag = Tag.objects.get(pk=pk)
            food = Food.objects.get(user=request.auth.user, pk=request.data["foodId"])

            food_tag, _ = FoodTag.objects.get_or_create(
                tag = tag,
                food = food
            )

            return Response({'message': 'tag added'}, status=status.HTTP_201_CREATED)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        method='DELETE',
        request_body=AddTagToFoodSerializer(),
        responses={
            204: openapi.Response(
                description="Returns message that tag was removed from food",
                schema=MessageSerializer()
            ),
            404: openapi.Response(
                description="Tag not found",
                schema=MessageSerializer()
            ),
        }
    )
    @action(methods=['delete'], detail=True)
    def remove_from_food(self, request, pk):
        """Add a tag to a current user's food"""
        try:

            tag = Tag.objects.get(pk=pk)
            food = Food.objects.get(user=request.auth.user, pk=request.data["foodId"])

            food_tag = FoodTag.objects.get(
                tag = tag,
                food = food
            )
            
            food_tag.delete()

            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
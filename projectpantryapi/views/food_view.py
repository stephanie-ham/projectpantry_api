
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projectpantryapi.models import Food, Location, Quantity, SafeFood
from projectpantryapi.serializers import (
    CreateFoodSerializer, FoodSerializer, MessageSerializer,
    SafeFoodSerializer)


class FoodView(ViewSet):
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The list of foods for the current user",
                schema=FoodSerializer(many=True)
            )
        },
        manual_parameters=[
            openapi.Parameter(
                "quantity_id",
                openapi.IN_QUERY,
                required=False,
                type=openapi.TYPE_INTEGER,
                description="Get foods by quantity"
            ),
            openapi.Parameter(
                "tag",
                openapi.IN_QUERY,
                required=False,
                type=openapi.TYPE_INTEGER,
                description="Get foods by tag"
            ),
        ]
    )
    def list(self, request):
        """Get a list of current user's foods"""
        foods = Food.objects.filter(user=request.auth.user)
        quantity = request.query_params.get('quantity_id', None)
        tag = request.query_params.get('tag', None)

        if quantity is not None:
            foods = foods.filter(quantity=quantity)

        if tag is not None:
            foods = foods.filter(tags=tag)

        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CreateFoodSerializer,
        responses={
            201: openapi.Response(
                description="Returns the created food",
                schema=FoodSerializer()
            ),
            400: openapi.Response(
                description="Validation Error",
                schema=MessageSerializer()
            )
        }
    )
    def create(self, request):
        """Create a food"""
        location = Location.objects.get(pk=request.data['locationId'])
        quantity = Quantity.objects.get(pk=request.data['quantityId'])
        try:
            food = Food.objects.create(
                name=request.data['name'],
                location=location,
                quantity=quantity,
                user=request.auth.user
            )
            serializer = FoodSerializer(food)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            204: openapi.Response(
                description="No content, food deleted successfully",
            ),
            404: openapi.Response(
                description="Food not found",
                schema=MessageSerializer()
            )
        }
    )
    @action(methods=['delete'], detail=True)
    def delete(self, request, pk):
        """Delete a food"""
        try:
            food = Food.objects.get(pk=pk, user=request.auth.user)
            food.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Food.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        # method='PUT',
        request_body=CreateFoodSerializer(),
        responses={
            204: openapi.Response(
                description="No Content, Food updated successfully"
            )
        }
    )
    # @action(methods=['PUT'], detail=False)
    def update(self, request, pk=None):
        """Update a food"""
        food = Food.objects.get(pk=pk, user=request.auth.user)
        location = Location.objects.get(pk=request.data['locationId'])
        quantity = Quantity.objects.get(pk=request.data['quantityId'])

        food.name = request.data['name'],
        food.location = location
        food.quantity = quantity

        food.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        method='POST',
        responses={
            201: openapi.Response(
                description="Returns message that food was added to safelist",
                schema=MessageSerializer()
            ),
            404: openapi.Response(
                description="Food not found",
                schema=MessageSerializer()
            ),
        }
    )
    @action(methods=['POST'], detail=True)
    def add_to_safelist(self, request, pk):
        """Add a food to the current user's SafeFood list"""
        food = Food.objects.get(pk=pk, user=request.auth.user)
        list_owner = request.auth.user
        try:
            safe_food = SafeFood.objects.create(
                list_owner=list_owner,
                food=food
            )
            serializer = SafeFoodSerializer(safe_food)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=True)
    def remove_from_safelist(self, request, pk):
        """Remove a food to the current user's SafeFood list"""
        try:
            food = Food.objects.get(pk=pk, user=request.auth.user)
            safe_food = SafeFood.objects.get(list_owner=request.auth.user)
            safe_food.food.remove(food)
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Food.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    # @swagger_auto_schema(
    #     responses={
    #         200: openapi.Response(
    #             description="A list of current user's foods filtered by quantity",
    #             schema=FoodSerializer(many=True)
    #         )
    #     }
    # )
    # @action(methods=['get'], detail=False)
    # def filter_by_quantity(self, request):
    #     """Handle GET requests to food by quantity"""

    #     foods = Food.objects.filter(user=request.auth.user)
    #     quantity = self.request.query_params.get('quantity_id', None)
    #     foods = foods.filter(quantity=quantity)

    #     serializer = FoodSerializer(foods, many=True)
    #     return Response(serializer.data)

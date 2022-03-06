from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projectpantryapi.models import Food, Location, Quantity
from projectpantryapi.serializers import CreateFoodSerializer,FoodSerializer, MessageSerializer

class FoodView(ViewSet):
    @swagger_auto_schema(responses={
        200: openapi.Response(
            description="The list of foods for the current user",
            schema=FoodSerializer(many=True)
        )
    })
    def list(self, request):
        """Get a list of current user's foods"""
        foods = Food.objects.filter(user=request.auth.user)
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
        location = Location.objects.get(pk=request.data['location'])
        quantity = Quantity.objects.get(pk=request.data['quantity'])
        try:
            food = Food.objects.create(
                name = request.data['name'],
                location = location,
                quantity = quantity,
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
                description="Tag not found",
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
        
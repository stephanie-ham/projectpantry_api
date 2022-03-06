from django import views
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projectpantryapi.models import Food
from projectpantryapi.serializers import FoodSerializer, MessageSerializer

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
    
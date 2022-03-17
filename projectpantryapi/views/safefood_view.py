from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projectpantryapi.models import SafeFood
from projectpantryapi.serializers import SafeFoodSerializer

class SafeFoodView(ViewSet):
    @swagger_auto_schema(responses={
        200: openapi.Response(
            description="The list of safe foods for the current user",
            schema=SafeFoodSerializer(many=True)
        )
    })
    def list(self, request):
        """Get a list of current user's safe foods"""
        safe_foods = SafeFood.objects.filter(list_owner=request.auth.user)

        serializer = SafeFoodSerializer(safe_foods, many=True)
        return Response(serializer.data)

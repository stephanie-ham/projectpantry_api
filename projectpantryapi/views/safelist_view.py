from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projectpantryapi.models import SafeList
from projectpantryapi.serializers import SafeListSerializer

class SafeListView(ViewSet):
    @swagger_auto_schema(responses={
        200: openapi.Response(
            description="The list of safe foods for the current user",
            schema=SafeListSerializer(many=True)
        )
    })
    def list(self, request):
        """Get a list of current user's safe foods"""
        safe_foods = SafeList.objects.filter(list_owner=request.auth.user)
        
        serializer = SafeListSerializer(safe_foods, many=True)
        return Response(serializer.data)

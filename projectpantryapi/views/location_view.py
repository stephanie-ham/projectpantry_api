
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projectpantryapi.models import Location
from projectpantryapi.serializers import LocationSerializer

class LocationView(ViewSet):
    @swagger_auto_schema(responses={
        200: openapi.Response(
            description="The list of locations",
            schema=LocationSerializer(many=True)
        )
    })

    def list(self, request):
        """Get a list of locations"""
        
        locations = Location.objects.all()
        
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
        
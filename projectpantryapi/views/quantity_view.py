
from statistics import quantiles
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projectpantryapi.models import Quantity
from projectpantryapi.serializers import QuantitySerializer

class QuantityView(ViewSet):
    @swagger_auto_schema(responses={
        200: openapi.Response(
            description="The list of quantities",
            schema=QuantitySerializer(many=True)
        )
    })

    def list(self, request):
        """Get a list of quantities"""
        
        quantities = Quantity.objects.all()
        
        serializer = QuantitySerializer(quantities, many=True)
        return Response(serializer.data)
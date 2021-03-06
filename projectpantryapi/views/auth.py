from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from projectpantryapi.serializers import CreateUserSerializer, MessageSerializer

@swagger_auto_schema(
    method= 'POST',
    request_body=AuthTokenSerializer(),
    responses={
        200: openapi.Response(
            description="Returns the newly created token",
            schema=AuthTokenSerializer()
        ),
        404: openapi.Response(
                description="The user was not found",
                schema=MessageSerializer()
        )
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)


@swagger_auto_schema(method='POST', request_body=CreateUserSerializer, responses={
    200: openapi.Response(
        description="Returns the newly created token",
        schema=AuthTokenSerializer()
    )
})
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new user for authentication
    '''

    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )

    token = Token.objects.create(user=new_user)
    data = {'token': token.key}
    return Response(data, status=status.HTTP_201_CREATED)

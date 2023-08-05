from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer


class LoginView(APIView):
    @swagger_auto_schema(
        operation_summary='Login',
        operation_description='User Login',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                'password': openapi.Schema(
                    type=openapi.TYPE_STRING
                )
            }
        )
    )
    def post(self, request, *args, **kwargs):
        refresh = None
        data = request.data
        username = data.get("username", "")
        password = data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            auth.login(request, user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


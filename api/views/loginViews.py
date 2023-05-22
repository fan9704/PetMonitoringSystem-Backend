from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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
                'user': userResponseConverter(user)
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


def userResponseConverter(user):
    if user is not None:
        result = dict(
            id=user.id,
            username=user.username,
            last_login=user.last_login,
            is_superuser=user.is_superuser,
            last_name=user.last_name,
            email=user.email,
            is_staff=user.is_staff,
            is_active=user.is_active,
            date_joined=user.date_joined,
            first_name=user.first_name)
    else:
        result = ""
    return result

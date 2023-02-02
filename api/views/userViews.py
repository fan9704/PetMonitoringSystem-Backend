from django.contrib.auth.models import User
from django.contrib import auth
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Register(APIView):
    @swagger_auto_schema(
        operation_summary='Register',
        operation_description='UserRegister',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                'password': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                'email': openapi.Schema(
                    type=openapi.TYPE_STRING
                )
            }
        )
    )
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get('email')
        print(username, email, password)
        user = User.objects.filter(email=email)
        print(user)

        if not user.exists():
            user = User.objects.create_user(username, email, password)
            print("success")
            return Response({
                "status": "success",
                "register": True,
                "user": userResponseConverter(user)
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    "register": False,
                    "message": "Duplicate Username or Email"
                },
                status=status.HTTP_409_CONFLICT
            )


class LoginAPI(APIView):
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
        data = request.data
        username = data.get("username", "")
        password = data.get("password", "")
        user = User.objects.get(username=username)
        print("Session", request.session.items(), "Cookie", request.COOKIES.items())
        try:
            if username == '' or password == '':
                return Response(
                    {"status": "Failed", "login": False, "error": "Account or Password cannot be empty"},
                    status=status.HTTP_406_NOT_ACCEPTABLE)
            authedUser = auth.authenticate(username=username, password=password)
            if authedUser:
                print(authedUser.username, "Has Authenticated")
                auth.login(request, authedUser)
                save = request.data.get('save', False)
                print(save)
                if save:
                    print("Session", request.session.items(), "Cookie", request.COOKIES.items())
                return Response({"status": "success", "login": True, "User": userResponseConverter(user)},
                                status=status.HTTP_200_OK)
            else:
                print("User: ", userResponseConverter(user), "Login Failed")
                return Response({"status": "failed", "login": False, "error": "Account or Password Error"},
                                status=status.HTTP_200_OK)

        except Exception as E:
            print(E)
            user = None
            print("User: ", username, "Login Failed")
        return Response({"status": "success", "login": True, "User": userResponseConverter(user)},
                        status=status.HTTP_200_OK)


class LogoutAPI(APIView):
    @swagger_auto_schema(
        operation_summary='Logout',
        operation_description='User Logout',
    )
    def get(self, request):
        auth.logout(request)
        print("Session", request.session.items(), "Cookie", request.COOKIES.items())
        return Response({"status": "success", "logout": True}, status=status.HTTP_200_OK)


class EditProfileAPI(APIView):
    @swagger_auto_schema(
        operation_summary='Edit Profile',
        operation_description='User Edit Profile',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                'password': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                'first_name': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                'last_name': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                'email': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
            }
        )
    )
    # permission_classes = [IsAuthenticated]
    def put(self, request):
        username = request.data.get("username", "")
        if username != '':
            user = User.objects.get(pk=username)
            if request.data["password"] != "":
                password = request.data["password"]
                user.set_password = password
            if request.data["first_name"] != "":
                first_name = request.data['first_name']
                user.first_name = first_name
            if request.data["last_name"] != "":
                last_name = request.data["last_name"]
                user.last_name = last_name
            if request.data["email"] != "":
                email = request.data["email"]
                user.email = email
            user.save()
            if user:
                return Response({"status": "success", "edit": True}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "edit": False}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request, pk):
        user_id = pk
        if user_id == '':
            return Response({"info": False}, status=status.HTTP_204_NO_CONTENT)
        else:
            user_id = int(user_id)
            user = User.objects.get(id=user_id)
            return Response(userResponseConverter(user), status=status.HTTP_200_OK)


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        userQuery = User.objects.all()
        userList = []
        for i in userQuery:
            userList.append(userResponseConverter(i))
        return Response(userList, status=status.HTTP_200_OK)


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

import datetime

from django.contrib.auth.models import User
from django.contrib import auth
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api import models
from api.serializers import PetSerializer, PetTypeSerializer


# Pet Type API
from api.views.userViews import userResponseConverter


class PetTypeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PetType.objects.all()
    serializer_class = PetTypeSerializer


class PetTypeCLAPIView(generics.ListCreateAPIView):
    queryset = models.PetType.objects.all()
    serializer_class = PetTypeSerializer


# Pet API

class PetRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pet.objects.all()
    serializer_class = PetSerializer


class PetCLAPIView(generics.ListCreateAPIView):
    queryset = models.Pet.objects.all()
    serializer_class = PetSerializer


class PetCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_summary='Create Pet',
        operation_description='Create Pet type and keeper should enter their ID',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                'keeper': openapi.Schema(
                    type=openapi.TYPE_NUMBER
                ),
                'type': openapi.Schema(
                    type=openapi.TYPE_NUMBER
                ),
                'birthday': openapi.Schema(
                    type=openapi.FORMAT_DATE
                ),
                'content': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
            }
        )
    )
    def post(self, request, *args, **kwargs):
        try:
            name = request.data.get("name", "")
            keeperId = request.data.get("keeper", 0)
            petTypeId = request.data.get("type", 0)
            birthday = request.data.get("birthday", datetime.date.today())
            content = request.data.get("content", "")

            keeper = User.objects.get(pk=keeperId)
            petType = models.PetType.objects.get(pk=petTypeId)

            pet = models.Pet.objects.create(
                name=name,
                keeper_id=keeper,
                type_id=petType,
                birthday=birthday,
                content=content
            )
            return Response(data=petResponseConverter(pet), status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(data=None, status=status.HTTP_404_NOT_FOUND)


def petResponseConverter(pet: models.Pet):
    if pet is not None:
        result = dict(
            id=pet.id,
            name=pet.name,
            keeper=userResponseConverter(pet.keeper),
            type_id=petTypeResponseConverter(pet.type),
            birthday=pet.birthday,
            content=pet.content
        )
    else:
        result = ""
    return result


def petTypeResponseConverter(petType: models.PetType):
    if petType is not None:
        result = dict(
            id=petType.id,
            typename=petType.typename,
            description=petType.description
        )
    else:
        result = ""
    return result

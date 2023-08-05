import datetime
import time

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


class PetListView(generics.ListAPIView):
    queryset = models.Pet.objects.all()
    serializer_class = PetSerializer


class PetQueryListView(APIView):
    def get(self, request, pet_type):
        pets = models.Pet.objects.filter(type__typename=pet_type)
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)


class PetCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_id='建立寵物',
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
                'size': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                'weight': openapi.Schema(
                    type=openapi.TYPE_NUMBER
                ),
                'gender': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                'is_neutered': openapi.Schema(
                    type=openapi.TYPE_BOOLEAN
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
            size = request.data.get("size", "")  # 取得新增欄位 size 的值
            weight = request.data.get("weight", 0)  # 取得新增欄位 weight 的值
            gender = request.data.get("gender", "")  # 取得新增欄位 gender 的值
            is_neutered = request.data.get("is_neutered", False)  # 取得新增欄位 is_neutered 的值

            keeper = User.objects.get(pk=keeperId)
            petType = models.PetType.objects.get(pk=petTypeId)

            # 計算每日熱量需求DER
            der = calculate_daily_energy_requirement(weight)

            pet = models.Pet.objects.create(
                name=name,
                keeper=keeper,
                type=petType,
                birthday=birthday,
                content=content,
                size=size,  # 使用新增欄位 size 的值
                weight=weight,  # 使用新增欄位 weight 的值
                gender=gender,  # 使用新增欄位 gender 的值
                is_neutered=is_neutered,  # 使用新增欄位 is_neutered 的值
                der=der,  # 儲存計算得到的 DER
            )
            return Response(data=petResponseConverter(pet), status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(data=None, status=status.HTTP_404_NOT_FOUND)


class PetCountAPIView(APIView):
    def get(self, request, *args, **kwargs):
        petDict = dict()
        for i in models.PetType.objects.all():
            petDict[i.typename] = models.Pet.objects.filter(type=i.id).count()
        return Response(data=petDict, status=status.HTTP_200_OK)


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


def calculate_resting_energy_requirement(weight):
    return 70 * (weight ** 0.75)


def calculate_daily_energy_requirement(weight, activity_level):
    activity_levels = {
        'low': 1.2,
        'moderate': 1.4,
        'high': 1.6,
    }

    if activity_level not in activity_levels:
        raise ValueError("Invalid activity level")

    levels = activity_levels[activity_level]
    return levels * calculate_resting_energy_requirement(weight)

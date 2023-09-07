import logging

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from api import models
from api.models import Pet
from api.serializers import PetSerializer, PetTypeSerializer, PetRequestSerializer, PetUploadImageSerializer

# Pet Type API

logger = logging.getLogger(__name__)


class PetTypeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PetType.objects.all()
    serializer_class = PetTypeSerializer


class PetTypeCLAPIView(generics.ListCreateAPIView):
    queryset = models.PetType.objects.all()
    serializer_class = PetTypeSerializer


# Pet API

class PetRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = models.Pet.objects.all()
    serializer_class = PetRequestSerializer


class PetListView(generics.ListAPIView):
    queryset = models.Pet.objects.all()
    serializer_class = PetSerializer


class PetQueryListView(APIView):
    def get(self, request: Request, pet_type):
        pets = models.Pet.objects.filter(type__typename=pet_type)
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)


class PetCreateAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        operation_id='建立寵物',
        operation_summary='Create Pet',
        operation_description='Create Pet type and keeper should enter their ID',
        request_body=PetRequestSerializer,
        manual_parameters=[
            openapi.Parameter(
                name='image',
                in_=openapi.IN_FORM,
                description='上傳的圖片',
                type=openapi.TYPE_FILE
            )
        ],
    )
    def post(self, request: Request, *args, **kwargs):
        serializer = PetRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.info(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)


class PetCountAPIView(APIView):
    def get(self, request: Request, *args, **kwargs):
        pet_dict = dict()
        for i in models.PetType.objects.all():
            pet_dict[i.typename] = models.Pet.objects.filter(type=i.id).count()
        return Response(data=pet_dict, status=status.HTTP_200_OK)


class PetUploadImageAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        operation_id='上傳寵物照片',
        operation_summary='Upload Pet Image',
        operation_description='Upload Pet Image By ID',
        request_body=PetUploadImageSerializer,
        manual_parameters=[
            openapi.Parameter(
                name='image',
                in_=openapi.IN_FORM,
                description='上傳的圖片',
                type=openapi.TYPE_FILE
            )
        ],
    )
    def post(self, request: Request, pk: int):
        try:
            pet = models.Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            logger.warning("Pet Upload Image Pet not found")
            return Response(data={'error': 'Pet not found'}, status=status.HTTP_404_NOT_FOUND)
        pet.image = request.FILES.get("image")
        pet.save()
        return Response(data=PetSerializer(pet).data, status=status.HTTP_200_OK)



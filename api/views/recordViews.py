from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics, viewsets
from rest_framework.response import Response

from api.models import Record, RecordType, Pet
from api.serializers import RecordSerializer, RecordTypeSerializer, RecordRequestSerializer


# RecordAPI
class RecordRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordListCreateView(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordRequestSerializer


class RecordByRecordType(viewsets.ViewSet):
    @swagger_auto_schema(
        tags=["record"],
        operation_id='透過RecordType搜尋所有Record',
        operation_summary='搜尋紀錄透過記錄種類',
        operation_description='需要帶入RecordType參數 種類名稱',
    )
    def recordType(self, request, record_type):
        try:
            record_type = RecordType.objects.get(type=record_type)
            records = Record.objects.filter(type=record_type)
            serializer = RecordSerializer(records, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RecordType.DoesNotExist:
            msg = {
                "message": "Not found Record Type"
            }
            return Response(msg, status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=["record"],
        operation_id='透過RecordType與Pet搜尋所有Record',
        operation_summary='搜尋紀錄透過寵物與記錄種類',
        operation_description='需要帶入RecordType與Pet參數 種類名稱',
    )
    def recordTypeAndPetName(self, request, record_type, pet_name):
        try:
            records = Record.objects.select_related('pet', 'type').filter(pet__name=pet_name, type__type=record_type)
            serializer = RecordSerializer(records, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RecordType.DoesNotExist:
            msg = {
                "message": "Not found Record Type"
            }
            return Response(msg, status.HTTP_404_NOT_FOUND)
        except Pet.DoesNotExist:
            msg = {
                "message": "Not found Pet"
            }
            return Response(msg, status.HTTP_404_NOT_FOUND)


# RecordTypeAPI
class RecordTypeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecordType.objects.all()
    serializer_class = RecordTypeSerializer


class RecordTypeListView(generics.ListAPIView):
    queryset = RecordType.objects.all()
    serializer_class = RecordTypeSerializer

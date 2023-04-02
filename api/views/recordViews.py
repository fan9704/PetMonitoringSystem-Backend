from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Record, RecordType, Pet
from api.serializers import RecordSerializer, RecordTypeSerializer


# RecordAPI
class RecordRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordListView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordByRecordType(APIView):
    @swagger_auto_schema(
        operation_id='透過RecordType搜尋所有Record',
        operation_summary='搜尋紀錄透過記錄種類',
        operation_description='需要帶入RecordType參數 種類名稱',
    )
    def get(self, request, recordType):
        try:
            recordTypeObject = RecordType.objects.get(type=recordType)
            records = Record.objects.filter(type=recordTypeObject)
            serializer = RecordSerializer(records, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as E:
            msg = {
                "message": "Not found Record Type"
            }
            return Response(msg, status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_id='透過RecordType與Pet搜尋所有Record',
        operation_summary='搜尋紀錄透過寵物與記錄種類',
        operation_description='需要帶入RecordType與Pet參數 種類名稱',
    )
    def get(self,request,recordType,petName):
        try:
            # pet = Pet.objects.get(name=petName)
            # recordTypeObject = RecordType.objects.get(type=recordType)
            # records = Record.objects.filter(type=recordTypeObject,pet=pet)
            records = Record.objects.select_related('pet','type').filter(pet__name=petName,type__type=recordType)
            serializer = RecordSerializer(records, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as E:
            msg = {
                "message": "Not found Record Type"
            }
            print(E)
            return Response(msg, status.HTTP_404_NOT_FOUND)


# RecordTypeAPI
class RecordTypeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecordType.objects.all()
    serializer_class = RecordTypeSerializer


class RecordTypeListView(generics.ListAPIView):
    queryset = RecordType.objects.all()
    serializer_class = RecordTypeSerializer

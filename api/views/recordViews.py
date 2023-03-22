from django.contrib.auth.models import User
from django.contrib import auth
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Record, RecordType
from api.serializers import RecordSerializer, RecordTypeSerializer


# RecordAPI
class RecordRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordListView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


# RecordTypeAPI
class RecordTypeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecordType.objects.all()
    serializer_class = RecordTypeSerializer


class RecordTypeListView(generics.ListAPIView):
    queryset = RecordType.objects.all()
    serializer_class = RecordTypeSerializer

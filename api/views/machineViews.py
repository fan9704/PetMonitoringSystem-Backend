from django.contrib.auth.models import User
from django.contrib import auth
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api import models
from api.serializers import MachineSerializer


# MachineAPI
class MachineRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Machine.objects.all()
    serializer_class = MachineSerializer


class MachineListView(generics.ListAPIView):
    queryset = models.Machine.objects.all()
    serializer_class = MachineSerializer

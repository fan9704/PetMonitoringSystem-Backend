from rest_framework import serializers
from api.models import Pet, PetType


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'keeper', 'type', 'birthday', 'content')
        read_only_fields = ('id',)


class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = ('id', 'typename', "description")
        read_only_fields = ('id',)

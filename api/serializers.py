from rest_framework import serializers
from api.models import Pet, PetType, Machine, RecordType, Record


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


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecordTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordType
        fields = ('id', 'type')
        read_only_fields = ('id',)


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('id', 'pet', 'type', 'data', 'machine')
        read_only_fields = ('id',)

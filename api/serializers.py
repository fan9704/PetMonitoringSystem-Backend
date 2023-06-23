from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Pet, PetType, Machine, RecordType, Record


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
        read_only_fields = ('id',)


class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = '__all__'
        read_only_fields = ('id',)


class PetSerializer(serializers.ModelSerializer):
    keeper = UserSerializer()
    type = PetTypeSerializer()

    class Meta:
        model = Pet
        fields = '__all__'
        read_only_fields = ('id',)
        depth = 1


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'
        read_only_fields = ('id',)
        depth = 1


class RecordTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordType
        fields = ('id', 'type')
        read_only_fields = ('id',)


class RecordSerializer(serializers.ModelSerializer):
    pet = PetSerializer()
    type = RecordTypeSerializer()

    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ('id',)
        depth = 1

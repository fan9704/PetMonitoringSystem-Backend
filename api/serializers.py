from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Pet, PetType, Machine, RecordType, Record, FcmToken


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


class PetRequestSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Pet
        fields = ['id', 'name', 'keeper', 'type', 'birthday', 'content', 'image']
        read_only_fields = ('id',)


class PetSerializer(serializers.ModelSerializer):
    keeper = UserSerializer()
    type = PetTypeSerializer()
    image = serializers.ImageField(required=False)

    class Meta:
        model = Pet
        fields = ['id', 'name', 'keeper', 'type', 'birthday', 'content', 'image']
        read_only_fields = ('id',)
        depth = 1


class PetUploadImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Pet
        fields = ['id', 'image']
        read_only_fields = ('id', 'name', 'keeper', 'type', 'birthday', 'content')
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


class FcmTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FcmToken
        fields = '__all__'

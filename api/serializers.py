from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone
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
        fields = ['id', 'name', 'keeper', 'type', 'birthday', 'content', 'image', 'weight', 'gender',
                  'is_neutered', 'activity_level', 'der']
        read_only_fields = ('id', 'der')

    def calculate_resting_energy_requirement(self, weight):
        return 70 * (weight ** 0.75)

    def calculate_daily_energy_requirement(self, weight, activity_level):
        activity_levels = {
            'low': 1.2,
            'moderate': 1.4,
            'high': 1.6,
        }

        if activity_level not in activity_levels:
            raise serializers.ValidationError("Invalid activity level")

        levels = activity_levels[activity_level]
        return levels * self.calculate_resting_energy_requirement(float(weight))

    def create(self, validated_data):
        weight = validated_data.get('weight', 0)
        activity_level = validated_data.get('activity_level')

        if activity_level:
            der = self.calculate_daily_energy_requirement(weight, activity_level)
            validated_data['der'] = der

        return super().create(validated_data)


class PetSerializer(serializers.ModelSerializer):
    keeper = UserSerializer()
    type = PetTypeSerializer()
    image = serializers.ImageField(required=False)

    class Meta:
        model = Pet
        fields = ['id', 'name', 'keeper', 'type', 'birthday', 'content', 'image', 'weight', 'gender',
                  'is_neutered', 'activity_level', ]
        read_only_fields = ('id',)
        depth = 1


class PetUploadImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Pet
        fields = ['id', 'image']
        read_only_fields = ('id', 'name', 'keeper', 'type', 'birthday', 'content', 'weight', 'gender',
                            'is_neutered', 'activity_level', 'der',)
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
        fields = '__all__'
        read_only_fields = ('id',)


class RecordSerializer(serializers.ModelSerializer):
    pet = PetSerializer()
    type = RecordTypeSerializer()

    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ('id',)
        depth = 1


class RecordRequestSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(
        default=datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%dT%H:%M:%S.%fZ'))

    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ('id',)


class FcmTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FcmToken
        fields = '__all__'

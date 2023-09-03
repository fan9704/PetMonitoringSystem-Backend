import logging

from rest_framework.exceptions import ValidationError
from django.test import TestCase
from api.serializers import PetTypeSerializer

logger = logging.getLogger(__name__)


def get_pet_type_valid_input():
    pet_type = {
        "typename": "cat",
        "description": "meow"
    }
    return pet_type


def get_pet_type_invalid_input():
    pet_type = {
    }
    return pet_type


class PetTypeSerializerTestCase(TestCase):
    def test_pet_type_serializer_valid(self):
        valid_pet_type = get_pet_type_valid_input()
        serializer = PetTypeSerializer(data=valid_pet_type)
        serializer.is_valid()

        # Assert
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['typename'], 'cat')
        self.assertEqual(serializer.validated_data['description'], 'meow')
        logger.debug("Complete PetType Serializer Test")

    def test_pet_type_serializer_invalid(self):
        invalid_pet_type = get_pet_type_invalid_input()
        serializer = PetTypeSerializer(data=invalid_pet_type)
        self.assertTrue(serializer.is_valid())
        logger.debug("Complete PetType Invalid Serializer Test")

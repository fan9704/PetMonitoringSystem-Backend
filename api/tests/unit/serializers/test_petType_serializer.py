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
        "typename": "",
        "description": "meow"
    }
    return pet_type


class PetTypeSerializerTestCase(TestCase):
    def test_petType_serializer(self):
        valid_pet_type = get_pet_type_valid_input()

        # Input JSON Data
        serializer = PetTypeSerializer(data=valid_pet_type)
        # Authenticate data valid
        serializer.is_valid()

        # Assert
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['typename'], 'cat')
        self.assertEqual(serializer.validated_data['description'], 'meow')
        logger.debug("Complete PetType Serializer Test")

        # # Input Invalid JSON Data
        # invalidPetType = getPetTypeInvalidInputJSON()
        # serializer = PetTypeSerializer(data=invalidPetType)
        # with self.assertRaises(ValidationError):
        #     serializer.is_valid(raise_exception=True)
        # logger.debug("Complete PetType Invalid Serializer Test")

import logging

from rest_framework.exceptions import ValidationError
from django.test import TestCase
from api.serializers import PetTypeSerializer

logger = logging.getLogger(__name__)


def getPetTypeValidInputJSON():
    petType = {
        "typename": "cat",
        "description": "meow"
    }
    return petType


def getPetTypeInvalidInputJSON():
    petType = {
        "typename": "",
        "description": "meow"
    }
    return petType


class PetTypeSerializerTestCase(TestCase):
    def test_petType_serializer(self):
        validPetType = getPetTypeValidInputJSON()

        # Input JSON Data
        serializer = PetTypeSerializer(data=validPetType)
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

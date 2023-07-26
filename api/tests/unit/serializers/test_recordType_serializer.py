import logging

from rest_framework.exceptions import ValidationError
from django.test import TestCase
from api.serializers import RecordTypeSerializer

logger = logging.getLogger(__name__)


def get_record_type_valid_input():
    data = {
        "type": "weight"
    }
    return data


def get_record_type_invalid_input():
    data = {
    }
    return data


class RecordTypeSerializerTestCase(TestCase):
    def test_petType_serializer(self):
        valid_data = get_record_type_valid_input()

        # Input JSON Data
        serializer = RecordTypeSerializer(data=valid_data)
        # Authenticate data valid
        serializer.is_valid()

        # Assert
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['type'], 'weight')
        logger.debug("Complete Record Type Serializer Test")

        # # Input Invalid JSON Data
        invalid_data = get_record_type_invalid_input()
        serializer = RecordTypeSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        logger.debug("Complete Record Type Invalid Serializer Test")

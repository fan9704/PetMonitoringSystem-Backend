import logging

from rest_framework.exceptions import ValidationError
from django.test import TestCase
from api.serializers import RecordSerializer
logger = logging.getLogger(__name__)


def get_record_valid_input():
    data = {
        "pet": {
            "id": 1,
            "keeper": {
                "username": "Aven",
                "first_name": "Wang",
                "last_name": "SZ"
            },
            "type": {
                "id": 1,
                "typename": "dog",
                "description": "string"
            },
            "name": "來福",
            "birthday": "2023-03-20",
            "content": "wow"
        },
        "type": {
            "id": 1,
            "type": "weight"
        },
        "data": 14
    }
    return data


def get_record_invalid_input():
    data = {
        "pet": {
            "id": 1,
            "keeper": {
                "username": "Aven",
                "first_name": "Wang",
                "last_name": "SZ"
            },
            "type": {
                "id": 1,
                "typename": "dog",
                "description": "string"
            },
            "name": "來福",
            "birthday": "2023-03-20",
            "content": "wow"
        },
        "data": 14
    }
    return data


class RecordSerializerTestCase(TestCase):
    def test_petType_serializer(self):
        valid_data = get_record_valid_input()

        # Input JSON Data
        serializer = RecordSerializer(data=valid_data)
        # Authenticate data valid
        serializer.is_valid()

        # Assert
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['pet']['type']['typename'], 'dog')
        self.assertEqual(serializer.validated_data['type']['type'], 'weight')
        self.assertEqual(serializer.validated_data['data'], 14)
        logger.debug("Complete Record Serializer Test")

        # # Input Invalid JSON Data
        invalid_data = get_record_invalid_input()
        serializer = RecordSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        logger.debug("Complete Record Invalid Serializer Test")

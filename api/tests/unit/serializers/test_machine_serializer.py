import logging

from rest_framework.exceptions import ValidationError
from django.test import TestCase
from api.serializers import MachineSerializer

logger = logging.getLogger(__name__)


def get_machine_valid_input():
    data = {
        "name": "TestD1",
        "onlineStatus": True,
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
    }
    return data


def get_machine_invalid_input():
    data = {
        "onlineStatus": True,
    }
    return data


class MachineSerializerTestCase(TestCase):
    def test_petType_serializer(self):
        valid_data = get_machine_valid_input()

        # Input JSON Data
        serializer = MachineSerializer(data=valid_data)
        # Authenticate data valid
        serializer.is_valid()

        # Assert
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], 'TestD1')
        self.assertEqual(serializer.validated_data['onlineStatus'], True)
        # self.assertEqual(serializer.validated_data['pet']['keeper']['username'], 'Aven')
        logger.debug("Complete Machine Serializer Test")

        # # Input Invalid JSON Data
        invalid_data = get_machine_invalid_input()
        serializer = MachineSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        logger.debug("Complete Machine Invalid Serializer Test")

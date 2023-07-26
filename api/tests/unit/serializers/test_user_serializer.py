import logging

from rest_framework.exceptions import ValidationError
from django.test import TestCase
from api.serializers import UserSerializer

logger = logging.getLogger(__name__)


class UserSerializerTestCase(TestCase):
    def test_user_serializer(self):
        user_data = {
            'username': 'john_doe',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        # Input JSON Data
        serializer = UserSerializer(data=user_data)
        # Authenticate data valid
        serializer.is_valid()

        # Assert
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['username'], 'john_doe')
        self.assertEqual(serializer.validated_data['first_name'], 'John')
        self.assertEqual(serializer.validated_data['last_name'], 'Doe')
        logger.debug("Complete User Serializer Test")

        # Input Invalid JSON Data
        invalid_user_data = {
            'username': '',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        serializer = UserSerializer(data=invalid_user_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        logger.debug("Complete User Invalid Serializer Test")

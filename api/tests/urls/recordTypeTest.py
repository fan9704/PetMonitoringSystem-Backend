from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import logging
from api.models import RecordType

logger = logging.getLogger(__name__)


class TodoListAPITest(APITestCase):

    def setUp(self):
        self.list_url = reverse('recordType-list')

        RecordType.objects.create(type="weight")
        RecordType.objects.create(type="water")
        RecordType.objects.create(type="humidity")
        RecordType.objects.create(type="temperature")
        RecordType.objects.create(type="food")

    def testRecordTypeList(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

        logger.debug("Complete Record Type URL Test")

    def tearDown(self):
        RecordType.objects.all().delete()

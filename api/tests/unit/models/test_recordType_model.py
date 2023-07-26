import logging
from django.test import TestCase
from api.models import RecordType

logger = logging.getLogger(__name__)


class RecordModelTest(TestCase):
    def setUp(self):
        RecordType.objects.create(type="weight")
        RecordType.objects.create(type="water")
        RecordType.objects.create(type="humidity")
        RecordType.objects.create(type="temperature")
        RecordType.objects.create(type="food")

    def testRecordTypeDescription(self):
        weightRecordType = RecordType.objects.get(type="weight")
        waterRecordType = RecordType.objects.get(type="water")
        humidityRecordType = RecordType.objects.get(type="humidity")
        temperatureRecordType = RecordType.objects.get(type="temperature")
        foodRecordType = RecordType.objects.get(type="food")

        # ID
        self.assertEqual(weightRecordType.id, 1)
        self.assertEqual(waterRecordType.id, 2)
        self.assertEqual(humidityRecordType.id, 3)
        self.assertEqual(temperatureRecordType.id, 4)
        self.assertEqual(foodRecordType.id, 5)
        logger.debug("Complete RecordType ID Model Test")
        # Description
        self.assertEqual(weightRecordType.type, "weight")
        self.assertEqual(waterRecordType.type, "water")
        self.assertEqual(humidityRecordType.type, "humidity")
        self.assertEqual(temperatureRecordType.type, "temperature")
        self.assertEqual(foodRecordType.type, "food")
        logger.debug("Complete RecordType Description Model Test")

    def tearDown(self):
        RecordType.objects.all().delete()

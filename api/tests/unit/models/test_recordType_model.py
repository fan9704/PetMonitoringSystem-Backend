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
        weight_record_type = RecordType.objects.get(type="weight")
        water_record_type = RecordType.objects.get(type="water")
        humidity_record_type = RecordType.objects.get(type="humidity")
        temperature_record_type= RecordType.objects.get(type="temperature")
        food_record_type = RecordType.objects.get(type="food")

        # ID
        self.assertEqual(weight_record_type.id, 1)
        self.assertEqual(water_record_type.id, 2)
        self.assertEqual(humidity_record_type.id, 3)
        self.assertEqual(temperature_record_type.id, 4)
        self.assertEqual(food_record_type.id, 5)
        logger.debug("Complete RecordType ID Model Test")
        # Description
        self.assertEqual(weight_record_type.type, "weight")
        self.assertEqual(water_record_type.type, "water")
        self.assertEqual(humidity_record_type.type, "humidity")
        self.assertEqual(temperature_record_type.type, "temperature")
        self.assertEqual(food_record_type.type, "food")
        logger.debug("Complete RecordType Description Model Test")

    def tearDown(self):
        RecordType.objects.all().delete()

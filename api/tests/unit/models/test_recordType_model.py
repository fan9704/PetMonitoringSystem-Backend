import logging
from django.test import TestCase
from api.models import RecordType

logger = logging.getLogger(__name__)


class RecordModelTest(TestCase):
    def setUp(self):
        self.weight_record_type = RecordType.objects.create(type="weight")
        self.water_record_type = RecordType.objects.create(type="water")
        self.humidity_record_type = RecordType.objects.create(type="humidity")
        self.temperature_record_type = RecordType.objects.create(type="temperature")
        self.food_record_type = RecordType.objects.create(type="food")

    def testRecordTypeDescription(self):
        # ID
        self.assertEqual(self.weight_record_type.id, 1)
        self.assertEqual(self.water_record_type.id, 2)
        self.assertEqual(self.humidity_record_type.id, 3)
        self.assertEqual(self.temperature_record_type.id, 4)
        self.assertEqual(self.food_record_type.id, 5)
        logger.debug("Complete RecordType ID Model Test")
        # Description
        self.assertEqual(self.weight_record_type.type, "weight")
        self.assertEqual(self.water_record_type.type, "water")
        self.assertEqual(self.humidity_record_type.type, "humidity")
        self.assertEqual(self.temperature_record_type.type, "temperature")
        self.assertEqual(self.food_record_type.type, "food")
        logger.debug("Complete RecordType Description Model Test")

    def testRecordTypeToString(self):
        self.assertEqual(str(self.weight_record_type), "類別:weight")
        self.assertEqual(str(self.water_record_type), "類別:water")
        self.assertEqual(str(self.humidity_record_type), "類別:humidity")
        self.assertEqual(str(self.temperature_record_type), "類別:temperature")
        self.assertEqual(str(self.food_record_type), "類別:food")
        logger.debug("Complete RecordType Model To String Test")

    def tearDown(self):
        RecordType.objects.all().delete()

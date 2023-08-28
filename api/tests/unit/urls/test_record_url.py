import logging

from django.test import TestCase
from django.urls import reverse

logger = logging.getLogger(__name__)


class RecordUrlTest(TestCase):
    def testRecordListByRecordTypeAndNameURL(self):
        record_type = "weight"
        pet_name = "cat1"
        url = reverse("record-listByRecordTypeAndPetName", args=[record_type, pet_name])
        self.assertEqual(url, f"/api/record/{record_type}/{pet_name}/")
        logger.debug("Complete Record List By RecordType and PetName URL Test")

    def testRecordListByRecordTypeURL(self):
        record_type = "weight"
        url = reverse('recordType', args=[record_type])
        self.assertEqual(url, f"/api/record/{record_type}/")
        logger.debug("Complete Record List By RecordType URL Test")

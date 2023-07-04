import logging

from django.test import TestCase
from django.urls import reverse

logger = logging.getLogger(__name__)


class RecordUrlTest(TestCase):
    def testRecordListByRecordTypeAndNameURL(self):
        recordType = "weight"
        petName = "cat1"
        url = reverse("record-listByRecordTypeAndPetName",args=[recordType,petName])
        self.assertEqual(url, f"/api/record/{recordType}/{petName}/")
        logger.debug("Complete Record List By RecordType and PetName URL Test")

    def testRecordListByRecordTypeURL(self):
        recordType = "weight"
        url = reverse('recordType', args=[recordType])
        self.assertEqual(url, f"/api/record/{recordType}/")
        logger.debug("Complete Record List By RecordType URL Test")
import logging

from django.test import TestCase
from django.urls import reverse

logger = logging.getLogger(__name__)


class RecordTypeUrlTest(TestCase):
    def testRecordTypeListURL(self):
        url = reverse("recordType-list")
        self.assertEqual(url, "/api/recordType/list/")
        logger.debug("Complete RecordType List URL Test")

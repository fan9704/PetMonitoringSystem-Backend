import logging

from django.test import TestCase
from django.urls import reverse

logger = logging.getLogger(__name__)


class MachineUrlTest(TestCase):
    def testMachineListURL(self):
        url = reverse("machine-list")
        self.assertEqual(url, f"/api/machine/list/")
        logger.debug("Complete Machine List URL Test")

    def testMachineRUDURL(self):
        pk = 1
        url = reverse("machine-rud", args=[pk])
        self.assertEqual(url, f"/api/machine/{pk}/")
        logger.debug("Complete Machine RUD URL Test")

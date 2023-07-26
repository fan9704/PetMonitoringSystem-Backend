import logging

from django.test import TestCase
from django.urls import reverse

logger = logging.getLogger(__name__)


class PetTypeUrlTest(TestCase):
    def testPetListCreateURL(self):
        url = reverse("petType-create-list")
        self.assertEqual(url, "/api/petType/")
        logger.debug("Complete PetType List-Create URL Test")

    def testPetRUDURL(self):
        pk = 1
        url = reverse('petType-rud', args=[pk])
        self.assertEqual(url, f"/api/petType/{pk}/")
        logger.debug("Complete PetType RUD URL Test")

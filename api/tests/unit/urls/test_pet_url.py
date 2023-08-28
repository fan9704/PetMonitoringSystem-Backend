import logging

from django.test import TestCase
from django.urls import reverse

logger = logging.getLogger(__name__)


class PetUrlTest(TestCase):
    def testPetListURL(self):
        url = reverse("pet-list")
        self.assertEqual(url, "/api/pet/list/")
        logger.debug("Complete Pet List URL Test")

    def testPetListByTypeURL(self):
        pet_type = "cat"
        url = reverse("pet-listByType", args=[pet_type])
        print(url)
        self.assertEqual(url, f"/api/pet/list/{pet_type}/")
        logger.debug("Complete Pet List By Type URL Test")

    def testPetRUDURL(self):
        pk = 1
        url = reverse('pet-rud', args=[pk])
        self.assertEqual(url, f"/api/pet/{pk}/")
        logger.debug("Complete Pet RUD URL Test")

    def testPetCreateURL(self):
        url = reverse('pet-create')
        self.assertEqual(url, "/api/pet/")
        logger.debug("Complete Pet Create URL Test")

    def testPetCountURL(self):
        url = reverse('pet-count')
        self.assertEqual(url, "/api/pet/count/pet_type/")
        logger.debug("Complete Pet Count URL Test")

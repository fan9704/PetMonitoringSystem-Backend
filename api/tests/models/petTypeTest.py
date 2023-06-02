import logging

from django.test import TestCase
from api.models import PetType

logger = logging.getLogger(__name__)


class PetModelTest(TestCase):
    def setUp(self):
        PetType.objects.create(typename="cat", description="貓咪")
        PetType.objects.create(typename="dog", description="狗")

    def testPetTypeName(self):
        catType = PetType.objects.get(typename="cat")
        dogType = PetType.objects.get(typename="dog")

        self.assertEqual(catType.typename, "cat")
        self.assertEqual(dogType.typename, "dog")
        print("Complete Test PetType Typename")

    def testPetTypeDescription(self):
        catType = PetType.objects.get(typename="cat")
        dogType = PetType.objects.get(typename="dog")

        self.assertEqual(catType.description, "貓咪")
        self.assertEqual(dogType.description, "狗")
        print("Complete Test PetType Description")

    def tearDown(self):
        PetType.objects.all().delete()

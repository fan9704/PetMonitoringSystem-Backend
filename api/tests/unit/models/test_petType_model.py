import logging

from django.test import TestCase
from api.models import PetType

logger = logging.getLogger(__name__)


class PetModelTest(TestCase):
    def setUp(self):
        PetType.objects.create(typename="cat", description="貓咪")
        PetType.objects.create(typename="dog", description="狗")

    def testPetTypeName(self):
        cat_type = PetType.objects.get(typename="cat")
        dog_type = PetType.objects.get(typename="dog")

        self.assertEqual(cat_type.typename, "cat")
        self.assertEqual(dog_type.typename, "dog")
        print("Complete Test PetType Typename")

    def testPetTypeDescription(self):
        cat_type = PetType.objects.get(typename="cat")
        dog_type = PetType.objects.get(typename="dog")

        self.assertEqual(cat_type.description, "貓咪")
        self.assertEqual(dog_type.description, "狗")
        print("Complete Test PetType Description")

    def tearDown(self):
        PetType.objects.all().delete()

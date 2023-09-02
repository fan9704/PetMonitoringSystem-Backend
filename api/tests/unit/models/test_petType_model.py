import logging

from django.test import TestCase
from api.models import PetType

logger = logging.getLogger(__name__)


class PetModelTest(TestCase):
    def setUp(self):
        self.cat_type = PetType.objects.create(typename="cat", description="貓咪")
        self.dog_type = PetType.objects.create(typename="dog", description="狗")

    def testPetTypeName(self):
        self.assertEqual(self.cat_type.typename, "cat")
        self.assertEqual(self.dog_type.typename, "dog")
        print("Complete Test PetType Typename")

    def testPetTypeDescription(self):
        self.assertEqual(self.cat_type.description, "貓咪")
        self.assertEqual(self.dog_type.description, "狗")
        print("Complete Test PetType Description")

    def testPetTypeToString(self):
        self.assertEqual(str(self.cat_type), "寵物種類cat")
        self.assertEqual(str(self.dog_type), "寵物種類dog")
        print("Complete Test PetType To String")

    def tearDown(self):
        PetType.objects.all().delete()

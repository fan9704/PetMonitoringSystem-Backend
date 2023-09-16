import datetime
import logging

from django.contrib.auth.models import User
from django.test import TestCase
from api.models import Pet, PetType, Machine

logger = logging.getLogger(__name__)


class MachineModelTest(TestCase):
    def setUp(self):
        cat_type = PetType.objects.create(typename="cat", description="貓咪")
        dog_type = PetType.objects.create(typename="dog", description="狗")

        u1 = User.objects.create(username="u1", email="u1@gmail.com")
        u2 = User.objects.create(username="u2", email="u2@gmail.com")

        cat1 = Pet.objects.create(name="cat1", keeper=u1, type=cat_type, birthday=datetime.date.today(),
                                       content="cat1")
        dog1 = Pet.objects.create(name="dog1", keeper=u2, type=dog_type, birthday=datetime.date.today(),
                                       content="dog1")

        self.m1 = Machine.objects.create(name="m1", onlineStatus=True, pet=cat1)
        self.m2 = Machine.objects.create(name="m2", onlineStatus=False, pet=dog1)

    def test_machine_properties(self):
        self.assertEqual(self.m1.name, "m1")
        self.assertEqual(self.m2.name, "m2")

        self.assertTrue(self.m1.onlineStatus)
        self.assertFalse(self.m2.onlineStatus)

        self.assertEqual(self.m1.pet.name, "cat1")
        self.assertEqual(self.m2.pet.name, "dog1")
        logger.debug("Complete Machine Model Test")

    def test_machine_to_string(self):
        self.assertEqual(str(self.m1),
                         f'機器名稱{self.m1.name} 狀態:{self.m1.onlineStatus} 綁定寵物:{self.m1.pet.name}')
        self.assertEqual(str(self.m2),
                         f'機器名稱{self.m2.name} 狀態:{self.m2.onlineStatus} 綁定寵物:{self.m2.pet.name}')
        logger.debug("Complete Machine Model To String Test")

    def tearDown(self):
        Pet.objects.all().delete()
        User.objects.all().delete()
        PetType.objects.all().delete()
        Machine.objects.all().delete()

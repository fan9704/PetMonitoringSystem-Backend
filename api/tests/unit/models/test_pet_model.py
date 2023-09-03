import datetime
import logging

from django.contrib.auth.models import User
from django.test import TestCase
from api.models import Pet, PetType

logger = logging.getLogger(__name__)


class PetModelTest(TestCase):
    def setUp(self):
        self.cat_type = PetType.objects.create(typename="cat", description="貓咪")
        self.dog_type = PetType.objects.create(typename="dog", description="狗")

        self.u1 = User.objects.create(username="u1", email="u1@gmail.com")
        self.u2 = User.objects.create(username="u2", email="u2@gmail.com")

        self.cat1 = Pet.objects.create(name="cat1", keeper=self.u1, type=self.cat_type, birthday=datetime.date.today(),
                                       content="cat1")
        self.cat2 = Pet.objects.create(name="cat2", keeper=self.u2, type=self.cat_type, birthday=datetime.date.today(),
                                       content="cat2")
        self.dog1 = Pet.objects.create(name="dog1", keeper=self.u1, type=self.dog_type, birthday=datetime.date.today(),
                                       content="dog1")
        self.dog2 = Pet.objects.create(name="dog2", keeper=self.u2, type=self.dog_type, birthday=datetime.date.today(),
                                       content="dog2")

    def testPetName(self):
        self.assertEqual(self.cat1.name, "cat1")
        self.assertEqual(self.dog1.name, "dog1")
        logger.debug("Complete Pet Name Model Test")

        self.assertEqual(self.cat1.keeper, self.u1)
        self.assertEqual(self.dog1.keeper, self.u1)
        logger.debug("Complete Pet Keeper Model Test")

        self.assertEqual(self.cat1.type, self.cat_type)
        self.assertEqual(self.dog1.type, self.dog_type)
        logger.debug("Complete Pet Type Model Test")

        self.assertEqual(self.cat1.birthday, datetime.date.today())
        self.assertEqual(self.dog1.birthday, datetime.date.today())
        logger.debug("Complete Pet Birthday Model Test")

        self.assertEqual(self.cat1.content, "cat1")
        self.assertEqual(self.dog1.content, "dog1")
        logger.debug("Complete Pet Content Model Test")

        self.assertEqual(str(self.cat1), f'{self.cat1.name}  照顧人:{self.cat1.keeper.username}:   寵物種類{self.cat1.type.typename}')
        self.assertEqual(str(self.dog1), f'{self.dog1.name}  照顧人:{self.dog1.keeper.username}:   寵物種類{self.dog1.type.typename}')

    def tearDown(self):
        Pet.objects.all().delete()
        User.objects.all().delete()
        PetType.objects.all().delete()

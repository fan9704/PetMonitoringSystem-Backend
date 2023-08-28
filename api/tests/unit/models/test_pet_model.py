import datetime
import logging

from django.contrib.auth.models import User
from django.test import TestCase
from api.models import Pet, PetType

logger = logging.getLogger(__name__)


class PetModelTest(TestCase):
    def setUp(self):
        cat_type = PetType.objects.create(typename="cat", description="貓咪")
        dog_type = PetType.objects.create(typename="dog", description="狗")

        u1 = User.objects.create(username="u1", email="u1@gmail.com")
        u2 = User.objects.create(username="u2", email="u2@gmail.com")

        Pet.objects.create(name="cat1", keeper=u1, type=cat_type, birthday=datetime.date.today(), content="cat1")
        Pet.objects.create(name="cat2", keeper=u2, type=cat_type, birthday=datetime.date.today(), content="cat2")
        Pet.objects.create(name="dog1", keeper=u1, type=dog_type, birthday=datetime.date.today(), content="dog1")
        Pet.objects.create(name="dog2", keeper=u2, type=dog_type, birthday=datetime.date.today(), content="dog2")

    def testPetName(self):
        cat1 = Pet.objects.get(name="cat1")
        dog1 = Pet.objects.get(name="dog1")

        u1 = User.objects.get(username="u1")

        cat_type = PetType.objects.get(typename="cat")
        dog_type = PetType.objects.get(typename="dog")

        self.assertEqual(cat1.name, "cat1")
        self.assertEqual(dog1.name, "dog1")
        logger.debug("Complete Pet Name Model Test")

        self.assertEqual(cat1.keeper, u1)
        self.assertEqual(dog1.keeper, u1)
        logger.debug("Complete Pet Keeper Model Test")

        self.assertEqual(cat1.type, cat_type)
        self.assertEqual(dog1.type, dog_type)
        logger.debug("Complete Pet Type Model Test")

        self.assertEqual(cat1.birthday, datetime.date.today())
        self.assertEqual(dog1.birthday, datetime.date.today())
        logger.debug("Complete Pet Birthday Model Test")

        self.assertEqual(cat1.content, "cat1")
        self.assertEqual(dog1.content, "dog1")
        logger.debug("Complete Pet Content Model Test")

        self.assertEqual(str(cat1), f'{cat1.name}  照顧人:{cat1.keeper.username}:   寵物種類{cat1.type.typename}')
        self.assertEqual(str(dog1), f'{dog1.name}  照顧人:{dog1.keeper.username}:   寵物種類{dog1.type.typename}')

    def tearDown(self):
        Pet.objects.all().delete()
        User.objects.all().delete()
        PetType.objects.all().delete()

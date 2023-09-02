import datetime
import logging

from django.contrib.auth.models import User
from django.test import TestCase
from api.models import Pet, PetType, Record, RecordType

logger = logging.getLogger(__name__)


class RecordModelTest(TestCase):
    def setUp(self):
        # PetType Fake Stub
        cat_type = PetType.objects.create(typename="cat", description="貓咪")
        dog_type = PetType.objects.create(typename="dog", description="狗")
        # User Fake Stub
        u1 = User.objects.create(username="u1", email="u1@gmail.com")
        u2 = User.objects.create(username="u2", email="u2@gmail.com")
        # Record Type Fake Stub
        weight_record_type = RecordType.objects.create(type="weight")
        water_record_type = RecordType.objects.create(type="water")
        humidity_record_type = RecordType.objects.create(type="humidity")
        temperature_record_type = RecordType.objects.create(type="temperature")
        food_record_type = RecordType.objects.create(type="food")
        # Pet Fake Stub
        self.cat1 = Pet.objects.create(name="cat1", keeper=u1, type=cat_type, birthday=datetime.date.today(), content="cat1")
        self.cat2 = Pet.objects.create(name="cat2", keeper=u2, type=cat_type, birthday=datetime.date.today(), content="cat2")
        self.dog1 = Pet.objects.create(name="dog1", keeper=u1, type=dog_type, birthday=datetime.date.today(), content="dog1")
        self.dog2 = Pet.objects.create(name="dog2", keeper=u2, type=dog_type, birthday=datetime.date.today(), content="dog2")
        # Data Dummy Stub
        weight_data = 0.6
        water_data = 0.7
        humidity_data = 0.8
        temperature_data = 0.9
        food_data = 1.0
        self.weight_record = Record.objects.create(
            pet=self.cat1,
            type=weight_record_type,
            data=weight_data
        )
        self.water_record = Record.objects.create(
            pet=self.cat2,
            type=water_record_type,
            data=water_data
        )
        self.humidity_record = Record.objects.create(
            pet=self.dog1,
            type=humidity_record_type,
            data=humidity_data
        )
        self.temperature_record = Record.objects.create(
            pet=self.dog2,
            type=temperature_record_type,
            data=temperature_data
        )
        self.food_record = Record.objects.create(
            pet=self.dog2,
            type=food_record_type,
            data=food_data
        )

    def testRecordFields(self):
        weight_data = 0.6
        water_data = 0.7
        humidity_data = 0.8
        temperature_data = 0.9
        food_data = 1.0

        # Name
        self.assertEqual(self.cat1.name, "cat1")
        self.assertEqual(self.dog1.name, "dog1")
        # Record
        self.assertEqual(self.weight_record.data, weight_data)
        self.assertEqual(self.water_record.data, water_data)
        self.assertEqual(self.humidity_record.data, humidity_data)
        self.assertEqual(self.temperature_record.data, temperature_data)
        self.assertEqual(self.food_record.data, food_data)
        logger.debug("Complete Pet Name Model Test")

    def test_record_to_string(self):
        self.assertEqual(str(self.weight_record), "數據0.6")
        self.assertEqual(str(self.water_record), "數據0.7")
        self.assertEqual(str(self.humidity_record), "數據0.8")
        self.assertEqual(str(self.temperate_record), "數據0.9")
        self.assertEqual(str(self.food_record), "數據1.0")

    def tearDown(self):
        # Clear Database
        PetType.objects.all().delete()
        User.objects.all().delete()
        RecordType.objects.all().delete()
        Pet.objects.all().delete()
        Record.objects.all().delete()

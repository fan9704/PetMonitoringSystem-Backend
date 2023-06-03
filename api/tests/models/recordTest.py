import datetime
import logging

from django.contrib.auth.models import User
from django.test import TestCase
from api.models import Pet, PetType, Record, RecordType

logger = logging.getLogger(__name__)

class RecordModelTest(TestCase):
    def setUp(self):
        # PetType Fake Stub
        catType = PetType.objects.create(typename="cat", description="貓咪")
        dogType = PetType.objects.create(typename="dog", description="狗")
        # User Fake Stub
        u1 = User.objects.create(username="u1", email="u1@gmail.com")
        u2 = User.objects.create(username="u2", email="u2@gmail.com")
        # Record Type Fake Stub
        weightRecordType = RecordType.objects.create(type="weight")
        waterRecordType = RecordType.objects.create(type="water")
        humidityRecordType = RecordType.objects.create(type="humidity")
        temperatureRecordType = RecordType.objects.create(type="temperature")
        foodRecordType = RecordType.objects.create(type="food")
        # Pet Fake Stub
        cat1 = Pet.objects.create(name="cat1", keeper=u1, type=catType, birthday=datetime.date.today(), content="cat1")
        cat2 = Pet.objects.create(name="cat2", keeper=u2, type=catType, birthday=datetime.date.today(), content="cat2")
        dog1 = Pet.objects.create(name="dog1", keeper=u1, type=dogType, birthday=datetime.date.today(), content="dog1")
        dog2 = Pet.objects.create(name="dog2", keeper=u2, type=dogType, birthday=datetime.date.today(), content="dog2")
        # Data Dummy Stub
        weightData = 0.6
        waterData = 0.7
        humidityData = 0.8
        temperatureData = 0.9
        foodData = 1.0
        Record.objects.create(
            pet=cat1,
            type=weightRecordType,
            data=weightData
        )
        Record.objects.create(
            pet=cat2,
            type=waterRecordType,
            data=waterData
        )
        Record.objects.create(
            pet=dog1,
            type=humidityRecordType,
            data=humidityData
        )
        Record.objects.create(
            pet=dog2,
            type=temperatureRecordType,
            data=temperatureData
        )
        Record.objects.create(
            pet=dog2,
            type=foodRecordType,
            data=foodData
        )

    def testRecordFields(self):
        cat1 = Pet.objects.get(name="cat1")
        cat2 = Pet.objects.get(name="cat2")
        dog1 = Pet.objects.get(name="dog1")
        dog2 = Pet.objects.get(name="dog2")

        u1 = User.objects.get(username="u1", email="u1@gmail.com")
        u2 = User.objects.get(username="u2", email="u2@gmail.com")

        weightRecordType = RecordType.objects.get(type="weight")
        waterRecordType = RecordType.objects.get(type="water")
        humidityRecordType = RecordType.objects.get(type="humidity")
        temperatureRecordType = RecordType.objects.get(type="temperature")
        foodRecordType = RecordType.objects.get(type="food")

        weightData = 0.6
        waterData = 0.7
        humidityData = 0.8
        temperatureData = 0.9
        foodData = 1.0

        weightRecord = Record.objects.get(
            pet=cat1,
            type=weightRecordType,
            data=weightData
        )
        waterRecord = Record.objects.get(
            pet=cat2,
            type=waterRecordType,
            data=waterData
        )
        humidityRecord = Record.objects.get(
            pet=dog1,
            type=humidityRecordType,
            data=humidityData
        )
        temperateRecord = Record.objects.get(
            pet=dog2,
            type=temperatureRecordType,
            data=temperatureData
        )
        foodRecord = Record.objects.get(
            pet=dog2,
            type=foodRecordType,
            data=foodData
        )

        # Name
        self.assertEqual(cat1.name, "cat1")
        self.assertEqual(dog1.name, "dog1")
        logger.debug("Complete Pet Name Model Test")

    def tearDown(self):
        # Clear Database
        PetType.objects.all().delete()
        User.objects.all().delete()
        RecordType.objects.all().delete()
        Pet.objects.all().delete()
        Record.objects.all().delete()

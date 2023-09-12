import logging
import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from api.views.recordViews import RecordByRecordType
from api.models import Record, RecordType, Pet, PetType

logger = logging.getLogger(__name__)


class RecordAPIViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.cat_type = PetType.objects.create(typename="cat", description="貓咪")
        self.weight_record_type = RecordType.objects.create(type="weight")
        self.u1 = User.objects.create(username="u1", email="u1@gmail.com")

    def tearDown(self) -> None:
        Record.objects.all().delete()
        RecordType.objects.all().delete()
        Pet.objects.all().delete()
        PetType.objects.all().delete()

    def test_list_record_valid(self):
        record_type = "weight"
        request = self.factory.get(path=f'/api/record/{record_type}/')

        view = RecordByRecordType.as_view({'get': 'recordType'})
        response = view(request, record_type=record_type)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_record_invalid(self):
        record_type = "w"
        request = self.factory.get(path=f'/api/record/{record_type}/')

        view = RecordByRecordType.as_view({'get': 'recordType'})
        response = view(request, record_type=record_type)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_record_by_record_type_valid(self):
        Pet.objects.create(name="cat12", keeper=self.u1, type=self.cat_type, birthday=datetime.date.today(),
                           content="cat12")
        record_type = "weight"
        pet_name = "cat12"
        request = self.factory.get(path=f'/api/record/{record_type}/{pet_name}/')

        view = RecordByRecordType.as_view({'get': 'recordTypeAndPetName'})
        response = view(request, record_type=record_type, pet_name=pet_name)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        logger.debug("Complete User Register with non-existing user")

    def test_list_record_by_record_type_invalid(self):
        Pet.objects.create(name="cat13", keeper=self.u1, type=self.cat_type, birthday=datetime.date.today(),
                           content="cat13")
        record_type = "wt"
        pet_name = "cat1"
        request = self.factory.get(path=f'/api/record/{record_type}/{pet_name}/')

        view = RecordByRecordType.as_view({'get': 'recordTypeAndPetName'})

        response = view(request, record_type=record_type, pet_name=pet_name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

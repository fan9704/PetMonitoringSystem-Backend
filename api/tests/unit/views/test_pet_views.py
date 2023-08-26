import logging
import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from PIL import Image
from io import BytesIO

from api.models import Pet, PetType
from api.serializers import PetSerializer
from api.views.petViews import PetListView,PetCreateAPIView,PetQueryListView,PetUploadImageAPIView

logger = logging.getLogger(__name__)


class PetAPIViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def tearDown(self) -> None:
        Pet.objects.all().delete()
        PetType.objects.all().delete()
        User.objects.all().delete()

    def test_list_pet(self):
        cat_type = PetType.objects.create(typename="cat", description="貓咪")
        dog_type = PetType.objects.create(typename="dog", description="狗")

        u1 = User.objects.create(username="u1", email="u1@gmail.com")
        u2 = User.objects.create(username="u2", email="u2@gmail.com")

        Pet.objects.create(name="cat1", keeper=u1, type=cat_type, birthday=datetime.date.today(), content="cat1")
        Pet.objects.create(name="cat2", keeper=u2, type=cat_type, birthday=datetime.date.today(), content="cat2")
        Pet.objects.create(name="dog1", keeper=u1, type=dog_type, birthday=datetime.date.today(), content="dog1")
        Pet.objects.create(name="dog2", keeper=u2, type=dog_type, birthday=datetime.date.today(), content="dog2")

        request = self.factory.get(path='/api/pet/list/')

        view = PetListView.as_view()
        response = view(request)

        logger.info(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

        logger.info("Complete test list pet")

    def test_create_pet_valid(self):
        data = {
            "name" : "cat3",
            "keeper":1,
            "type":1,
            "content":"test for create pet"
        }
        request = self.factory.post(path="/api/pet/",data=data, format='multipart')

        view = PetCreateAPIView.as_view()
        response = view(request)

        logger.info(response.data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'],'cat3' )

    def test_create_pet_invalid(self):
        data = {
            "name": "cat3",
        }
        request = self.factory.post(path="/api/pet/", data=data, format='multipart')

        view = PetCreateAPIView.as_view()
        response = view(request)

        logger.info(response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_count_pet(self):
        PetType.objects.create(typename="cat", description="貓咪")
        PetType.objects.create(typename="dog", description="狗")
        PetType.objects.create(typename="mouse", description="鼠")
        PetType.objects.create(typename="other", description="其他")
        request = self.factory.get(path="/api/count/petType/")

        view = PetQueryListView
        response = view(request)

        logger.info(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data.keys()),4)

    def test_upload_pet_image(self):
        image = Image.new('RGB', (100, 100))
        image_io = BytesIO()
        image.save(image_io, 'JPEG')
        image_io.seek(0)

        url = reverse('pet-upload-image', args=[self.pet.pk])
        request = self.factory.post(url, {'image': image_io}, format='multipart')

        view = PetUploadImageAPIView.as_view()
        response = view(request, pk=self.pet.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.pet.refresh_from_db()
        self.assertIsNotNone(self.pet.image)

        expected_data = PetSerializer(self.pet).data
        self.assertEqual(response.data, expected_data)
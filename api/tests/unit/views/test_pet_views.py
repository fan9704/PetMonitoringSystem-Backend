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
from api.views.petViews import PetListView, PetCreateAPIView, PetQueryListView, PetUploadImageAPIView, PetCountAPIView

logger = logging.getLogger(__name__)


class PetAPIViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.u1 = User.objects.create(username="u1", email="u1@gmail.com")
        self.u2 = User.objects.create(username="u2", email="u2@gmail.com")
        self.cat_type = PetType.objects.create(typename="cat", description="貓咪")
        self.dog_type = PetType.objects.create(typename="dog", description="狗")
        self.mouse_type = PetType.objects.create(typename="mouse", description="鼠")
        self.other_type = PetType.objects.create(typename="other", description="其他")

        image = Image.new('RGB', (100, 100))
        self.image_io = BytesIO()
        image.save(self.image_io, 'JPEG')
        self.image_io.seek(0)


    def tearDown(self) -> None:
        Pet.objects.all().delete()
        PetType.objects.all().delete()
        User.objects.all().delete()

    def test_list_pet(self):
        Pet.objects.create(name="cat1", keeper=self.u1, type=self.cat_type, birthday=datetime.date.today(),
                           content="cat1")
        Pet.objects.create(name="cat2", keeper=self.u2, type=self.cat_type, birthday=datetime.date.today(),
                           content="cat2")
        Pet.objects.create(name="dog1", keeper=self.u1, type=self.dog_type, birthday=datetime.date.today(),
                           content="dog1")
        Pet.objects.create(name="dog2", keeper=self.u2, type=self.dog_type, birthday=datetime.date.today(),
                           content="dog2")

        request = self.factory.get(path='/api/pet/list/')

        view = PetListView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

        logger.info("Complete test list pet")

    def test_list_pet_by_pet_type(self):
        Pet.objects.create(name="cat12", keeper=self.u1, type=self.cat_type, birthday=datetime.date.today(),
                           content="cat12")
        target_pet_type = "cat'"
        request = self.factory.get(path=f'/api/pet/list/{target_pet_type}')

        view = PetQueryListView.as_view()
        response = view(request, pet_type=target_pet_type)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.info("Complete test list pet by pet type")

    def test_create_pet_valid(self):
        data = {
            "name": "cat3",
            "keeper": self.u1.id,
            "type": self.cat_type.id,
            "content": "test for create pet"
        }

        request = self.factory.post(path="/api/pet/", data=data, format='multipart')

        view = PetCreateAPIView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'cat3')

    def test_create_pet_invalid(self):
        data = {
            "name": "cat3",
        }
        request = self.factory.post(path="/api/pet/", data=data, format='multipart')

        view = PetCreateAPIView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_count_pet(self):
        request = self.factory.get(path="/api/count/pet_type/")

        view = PetCountAPIView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.keys()), 4)

    def test_upload_pet_image(self):
        pet = Pet.objects.create(name="cat1", keeper=self.u1, type=self.cat_type, birthday=datetime.date.today(),
                                 content="cat1")
        url = reverse('pet-upload-image', args=[pet.id])
        request = self.factory.post(url, {'image': self.image_io}, format='multipart')

        view = PetUploadImageAPIView.as_view()
        response = view(request, pk=pet.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data["image"])

    def test_upload_pet_image_invalid(self):
        url = reverse('pet-upload-image', args=[50])
        request = self.factory.post(url, {'image': self.image_io}, format='multipart')

        view = PetUploadImageAPIView.as_view()
        response = view(request, pk=50)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data.error, 'Pet not found')

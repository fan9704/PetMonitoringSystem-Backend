import datetime
import json

from django.urls import include, path, reverse
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from api.models import Pet, PetType

import logging

logger = logging.getLogger(__name__)


class PetUrlTest(TestCase):
    def setUp(self):
        catType = PetType.objects.create(typename="cat", description="貓咪")
        dogType = PetType.objects.create(typename="dog", description="狗")

        u1 = User.objects.create(username="u1", email="u1@gmail.com")
        u2 = User.objects.create(username="u2", email="u2@gmail.com")

        Pet.objects.create(name="cat1", keeper=u1, type=catType, birthday=datetime.date.today(), content="cat1")
        Pet.objects.create(name="cat2", keeper=u2, type=catType, birthday=datetime.date.today(), content="cat2")
        Pet.objects.create(name="dog1", keeper=u1, type=dogType, birthday=datetime.date.today(), content="dog1")
        Pet.objects.create(name="dog2", keeper=u2, type=dogType, birthday=datetime.date.today(), content="dog2")

    def testCreatePet(self):
        data = {
            "name": "cat3",
            "keeper": 1,
            "type": 1,
            "birthday": "2023-02-02",
            "content": "string"
        }
        response = self.client.post('/api/pet/',
                                    data=data,
                                    format='json', )
        logger.debug(response.status_code)
        logger.debug(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["id"], 5)

    # def testGetPet(self):
    #     response = self.client.get('/api/pet/1/', format='json')
    #     logger.debug(response.status_code)
    #     logger.debug(response.content)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data["id"], 1)
    #
    # def testUpdatePet(self):
    #     data = {
    #         "name": "cat8",
    #         "keeper": 1,
    #         "type": 1,
    #         "birthday": "2023-02-02",
    #         "content": "string"
    #     }
    #     response = self.client.put('/api/pet/1/',
    #                                data=data)
    #     logger.debug(response.status_code)
    #     logger.debug(response.content)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data["name"], "cat8")

    def testListPet(self):
        response = self.client.get('/api/pet/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
        logger.debug("Complete Test List Pet")

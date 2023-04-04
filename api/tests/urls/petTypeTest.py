import logging

from django.test import TestCase

from api.models import PetType

logger = logging.getLogger(__name__)


class PetUrlTest(TestCase):
    def setUp(self):
        PetType.objects.create(typename="cat", description="貓咪")
        PetType.objects.create(typename="dog", description="狗")

    def testCreatePetType(self):
        data = {
            "typename": "bird",
            "description": "鳥"
        }
        response = self.client.post('/api/petType/',
                                    data=data,
                                    format='json', )
        logger.debug(response.status_code)
        logger.debug(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(type(response.data["id"]), type(3))

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

    def testListPetType(self):
        response = self.client.get('/api/petType/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        logger.debug("Complete Test List PetType")

import logging

from django.core.management import call_command
from django.test import TestCase
from elasticsearch_dsl import Index

from api.documents import UserES, PetES

logger = logging.getLogger(__name__)


class UpdateElasticsearchDataTestCase(TestCase):
    def setUp(self) -> None:
        self.user_index = Index('user')
        self.pet_index = Index('pet')

        if self.user_index.exists():
            self.user_index.delete()
        if self.pet_index.exists():
            self.pet_index.delete()

        self.user_index.create()
        self.pet_index.create()

        logger.info("Initialize Elasticsearch Index")

    def tearDown(self):
        if self.user_index.exists():
            self.user_index.delete()
        if self.pet_index.exists():
            self.pet_index.delete()

        logger.info("Delete Elasticsearch Index")

    def test_update_elasticsearch_data(self):
        call_command('update_es_data')

        user_index = UserES._index
        self.assertTrue(user_index.exists())
        logger.info("User Elasticsearch Index Exist")

        pet_index = PetES._index
        self.assertTrue(pet_index.exists())
        logger.info("Pet Elasticsearch Index Exist")

        logger.info("Complete Test Commands Update ES Data")

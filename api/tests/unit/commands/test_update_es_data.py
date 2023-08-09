import logging
import os

from django.core.management import call_command
from django.test import TestCase
from elasticsearch_dsl import Index
from dotenv import load_dotenv, find_dotenv

from api.documents import UserES, PetES

logger = logging.getLogger(__name__)
load_dotenv(find_dotenv())


class UpdateElasticsearchDataTestCase(TestCase):
    es_enabled = os.getenv("ELASTICSEARCH_ENABLE",False)
    CLOSED_STATEMENT = "Elasticsearch in Closed Statement"
    def setUp(self) -> None:
        if self.es_enabled:
            self.user_index = Index('user')
            self.pet_index = Index('pet')

            if self.user_index.exists():
                self.user_index.delete()
            if self.pet_index.exists():
                self.pet_index.delete()

            self.user_index.create()
            self.pet_index.create()

            logger.info("Initialize Elasticsearch Index")
        else:
            logger.info(self.CLOSED_STATEMENT)

    def tearDown(self):
        if self.es_enabled:
            if self.user_index.exists():
                self.user_index.delete()
            if self.pet_index.exists():
                self.pet_index.delete()

            logger.info("Delete Elasticsearch Index")
        else:
            logger.info(self.CLOSED_STATEMENT)

    def test_update_elasticsearch_data(self):
        if self.es_enabled:
            call_command('update_es_data')

            user_index = UserES._index
            self.assertTrue(user_index.exists())
            logger.info("User Elasticsearch Index Exist")

            pet_index = PetES._index
            self.assertTrue(pet_index.exists())
            logger.info("Pet Elasticsearch Index Exist")

            logger.info("Complete Test Commands Update ES Data")
        else:
            logger.info(self.CLOSED_STATEMENT)
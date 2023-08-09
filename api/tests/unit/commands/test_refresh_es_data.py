import unittest
import os
import logging

from django.core.management import call_command
from elasticsearch_dsl import Index
from dotenv import load_dotenv, find_dotenv

logger = logging.getLogger(__name__)
load_dotenv(find_dotenv())

class RefreshESDataTestCase(unittest.TestCase):
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
        else:
            logger.info(self.CLOSED_STATEMENT)
    def tearDown(self) -> None:
        if self.es_enabled:
            self.user_index.delete()
            self.pet_index.delete()
        else:
            logger.info(self.CLOSED_STATEMENT)
    def test_refresh_es(self):
        if self.es_enabled:
            call_command('refresh_es')

            self.assertTrue(self.user_index.exists())
            self.assertTrue(self.pet_index.exists())
        else:
            logger.info(self.CLOSED_STATEMENT)
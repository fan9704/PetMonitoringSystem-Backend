from django.core.management.base import BaseCommand
from elasticsearch_dsl import Index
import os
import logging

from api.documents import UserES, PetES

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Refresh data in Elasticsearch'
    es_enabled = os.getenv("ELASTICSEARCH_ENABLE", False)

    def handle(self, *args, **kwargs):
        if self.es_enabled:
            UserES.init()
            Index('user').refresh()
            PetES.init()
            Index('pet').refresh()
            logger.info("Elasticsearch Refreshed")
        else:
            logger.info("Elasticsearch is Closed")

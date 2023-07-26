import os

from django.core.management.base import BaseCommand
from elasticsearch_dsl import Index
from api.documents import UserES, PetTypeES,PetES


class Command(BaseCommand):
    help = 'Refresh data in Elasticsearch'

    def handle(self, *args, **kwargs):
        UserES.init()
        Index('user').refresh()
        PetES.init()
        Index('pet').refresh()

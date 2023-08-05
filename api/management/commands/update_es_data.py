import logging
import os

from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
from api.models import Record, Pet, RecordType

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Update data in Elasticsearch'
    es = Elasticsearch(hosts=os.getenv("ELASTICSEARCH_ENDPOINT"))

    def handle(self, *args, **kwargs):
        self.update_record_es_data()
        self.update_pet_es_data()
        logger.info('Update data in Elasticsearch Complete')

    def update_record_es_data(self):
        all_records = Record.objects.all()
        for record in all_records:
            type_dict = {
                'id': record.type.id,
                'typename': record.type.type,
            }
            pet_dict = {
                'id': record.pet.id,
                'name': record.pet.name,
                'keeper': {
                    'id': record.pet.keeper.id,
                    'first_name': record.pet.keeper.first_name,
                    'last_name': record.pet.keeper.last_name,
                    'username': record.pet.keeper.username,
                },
                'type': {
                    'id': record.pet.type.id,
                    'typename': record.pet.type.typename,
                    'description': record.pet.type.description,
                },
                'birthday': record.pet.birthday,
                'content': record.pet.content,
            }
            # 使用 Elasticsearch 原生 API 更新 Document
            self.es.update(index='record', doc_type='_doc', refresh=True, id=record.id, body={"doc":{
                'pet': pet_dict,
                'type': type_dict,
                'time': record.time,
                'data': record.data,
            }})

    def update_pet_es_data(self):
        all_pets = Pet.objects.all()
        for pet in all_pets:
            pet_dict = {
                'id': pet.id,
                'name': pet.name,
                'keeper': {
                    'id': pet.keeper.id,
                    'first_name': pet.keeper.first_name,
                    'last_name': pet.keeper.last_name,
                    'username': pet.keeper.username,
                },
                'type': {
                    'id': pet.type.id,
                    'typename': pet.type.typename,
                    'description': pet.type.description,
                },
                'birthday': pet.birthday,
                'content': pet.content,
            }
            self.es.update(index='pet', doc_type='_doc', id=pet.id, body={"doc":pet_dict})

    def update_record_type_es_data(self):
        RecordType.objects.all()

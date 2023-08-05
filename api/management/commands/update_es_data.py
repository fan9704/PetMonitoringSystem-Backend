import logging
import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from elasticsearch import Elasticsearch
from api.models import Record, Pet, RecordType, PetType

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Update data in Elasticsearch'
    es = Elasticsearch(hosts=os.getenv("ELASTICSEARCH_ENDPOINT"))

    def handle(self, *args, **kwargs):
        self.update_record_es_data()
        self.update_record_type_es_data()
        self.update_pet_es_data()
        self.update_pet_type_es_data()
        self.update_user_es_data()
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

    def update_pet_type_es_data(self):
        pet_types = PetType.objects.all()
        for pet_type in pet_types:
            pet_type_dict = {
                'id': pet_type.id,
                'typename': pet_type.typename,
                'description': pet_type.description
            }

            self.es.update(index='pet_type', doc_type='_doc', id=pet_type.id, body={"doc":pet_type_dict})

    def update_record_type_es_data(self):
        record_types = RecordType.objects.all()
        for record_type in record_types:
            record_types_dict = {
                'id': record_type.id,
                'type': record_type.type
            }
            self.es.update(index='record_type', doc_type='_doc', id=record_type.id, body={"doc":record_types_dict})

    def update_user_es_data(self):
        users = User.objects.all()
        for user in users:
            user_dict = {
                'id': user.id,
                'password': user.password,
                'last_login': user.last_login,
                'is_superuser': user.is_superuser,
                'username': user.username,
                "first_name": user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'data_joined': user.date_joined

            }

            self.es.update(index='user', doc_type='_doc', refresh=True, id=user.id, body={"doc":user_dict})

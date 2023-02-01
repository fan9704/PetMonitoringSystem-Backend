from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from api.models import Pet, PetType


@registry.register_document
class UserES(Document):
    class Index:
        name = 'user'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
        ]


@registry.register_document
class PetTypeES(Document):
    class Index:
        name = 'type'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = PetType
        fields = [
            'id',
            'typename',
            'description',
        ]


@registry.register_document
class PetES(Document):
    keeper = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })
    petType = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'typename': fields.TextField(),
        'description': fields.TextField(),
    })
    type = fields.TextField(attr='type_to_string')

    class Index:
        name = 'pet'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Pet
        fields = [
            'id',
            'name',
            'birthday',
            'content',
        ]

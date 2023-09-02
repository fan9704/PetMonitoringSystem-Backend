from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from api.models import Pet, PetType, Record, RecordType


@registry.register_document
class UserES(Document):
    class Index:
        name = 'user'
        settings = {
            'number_of_shards': 1,  # 分片 分在不同 Node
            'number_of_replicas': 0,  # 副本 同一 Node 有幾個
        }

    class Django:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'password',
            'last_login',
            'is_staff',
            'is_superuser',
        ]
        auto_refresh = True


@registry.register_document
class PetTypeES(Document):
    class Index:
        name = 'pet_type'
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
            'weight',
            'gender',
            'is_neutered',
            'activity_level',
            'der'
        ]


@registry.register_document
class RecordES(Document):
    pet = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
        'keeper': fields.ObjectField(properties={
            'id': fields.IntegerField(),
            'first_name': fields.TextField(),
            'last_name': fields.TextField(),
            'username': fields.TextField(),
        }),
        'type': fields.ObjectField(properties={
            'id': fields.IntegerField(),
            'typename': fields.TextField(),
            'description': fields.TextField(),
        }),
        'birthday': fields.DateField(),
        'content': fields.TextField(),
    })

    type = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'typename': fields.TextField(),
    })

    class Index:
        name = 'record'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Record
        fields = [
            'id',
            'data',
            'time'
        ]


@registry.register_document
class RecordTypeES(Document):
    class Index:
        name = 'record_type'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = RecordType
        fields = [
            'id',
            'type'
        ]

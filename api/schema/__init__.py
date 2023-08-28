import graphene

from api.models import RecordType
from api.schema.RecordType import CreateRecordType, RecordTypeQL


class Mutation(graphene.ObjectType):
    create_record_type = CreateRecordType.Field()


class Query(graphene.ObjectType):
    record_types = graphene.List(RecordTypeQL, type=graphene.String())

    def resolve_record_types(self, info, **kwargs):
        _type = kwargs.get('type')
        if _type is not None:
            return RecordType.objects.filter(type__contains=_type)
        return RecordType.objects.all()

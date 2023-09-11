import graphene

from api.models import RecordType
from api.schema.RecordTypeSchema import CreateRecordType, RecordTypeQL


class Mutation(graphene.ObjectType):
    create_record_type = CreateRecordType.Field()


class Query(graphene.ObjectType):
    all_record_type = graphene.List(RecordTypeQL)

    def resolve_all_record_type(self, info, **kwargs):
        return RecordType.objects.all()

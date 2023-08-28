import graphene
from graphene_django.types import DjangoObjectType
from api.models import RecordType


class RecordTypeQL(DjangoObjectType):
    class Meta:
        model = RecordType


class RecordTypeDTO(graphene.InputObjectType):
    type = graphene.String()


class CreateRecordType(graphene.Mutation):
    class Arguments:
        record_type_data = RecordTypeDTO()

    success = graphene.Boolean()
    record_type = graphene.Field(RecordTypeQL)

    def mutate(self, info, record_type_data):
        record_type = RecordType(
            type=record_type_data.type
        )
        record_type.save()
        return CreateRecordType(record_type=record_type, success=True)



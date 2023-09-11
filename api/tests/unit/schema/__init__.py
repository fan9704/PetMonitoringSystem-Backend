import logging

from django.test.utils import TestCase
from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase
from PetMonitoringSystemBackend.schema import schema

logger = logging.getLogger(__name__)


class RecordTypeQLTestCase(GraphQLTestCase):
    def setUp(self) -> None:
        self.client = Client(schema)

    def test_record_type_query(self):
        executed = self.client.execute(
            '''
            query {
              allRecordType{
                  id
                  type
              }
            }
            ''',
        )
        self.assertIsNotNone(executed)

    def test_record_type_mutation(self):
        executed = self.client.execute(
            '''
            mutation {
              createRecordType(recordTypeData: {type: "heartbeat"}) {
                success
                recordType {
                  id
                  type
                }
              }
            }
            ''',
        )

        self.assertIsNotNone(executed)

from django.test import TestCase
from graphene.test import Client
from api import schema
from api.models import RecordType


class RecordTypeQueryTestCase(TestCase):
    def setUp(self):
        self.water_record_type = RecordType.objects.create(type="water")
        self.food_record_type = RecordType.objects.create(type="food")
        self.client = Client(schema)

    def test_record_types_query(self):
        query = """
        query {
          recordTypes(type: "water") {
            type
          }
        }
        """

        response = self.client.execute(query)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data']['recordTypes'][0]['type'], "water")

    def test_record_types_query_all(self):
        query = """
        query {
          recordTypes {
            type
          }
        }
        """

        response = self.client.execute(query)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['data']['recordTypes']), 2)

# GraphQL Unittest

### django-graphene unittest

> Test failed

```python
from graphene_django.utils.testing import GraphQLTestCase

class RecordTypeQLTestCase(GraphQLTestCase):
    def test_record_type_query(self):
        response = self.query(
            '''
            query {
              allRecordType{
                  id
                  type
              }
            }
            ''',
        )

        self.assertResponseNoErrors(response)
        self.assertEqual(response.status_code, 200)

    def test_record_type_mutation(self):
        response = self.query(
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

        self.assertResponseNoErrors(response)
```
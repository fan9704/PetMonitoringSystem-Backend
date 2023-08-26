from django.core.management import call_command
from django.test import TransactionTestCase
from django.db import connections
from psycopg2 import sql


class CreateTestDatabaseTestCase(TransactionTestCase):
    def test_create_test_database(self):
        call_command('create_test_db')

        with connections['default'].cursor() as cursor:
            query = sql.SQL("SELECT datname FROM pg_database WHERE datname = %s;")
            cursor.execute(query, ['test'])
            database_exists = cursor.fetchone()

        self.assertIsNotNone(database_exists)

    def tearDown(self):
        with connections['default'].cursor() as cursor:
            query = sql.SQL("DROP DATABASE IF EXISTS test;")
            cursor.execute(query)

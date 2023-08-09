from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import ProgrammingError


class Command(BaseCommand):
    help = 'Create a PostgreSQL database named "test" for testing'

    def handle(self, *args, **options):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT datname FROM pg_database WHERE datname = 'test';")
                database_exists = cursor.fetchone()
        except ProgrammingError:
            database_exists = False

        if not database_exists:
            with connection.cursor() as cursor:
                cursor.execute('CREATE DATABASE TEST;')
            self.stdout.write(self.style.SUCCESS('Database "test" created successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('Database "test" already exists.'))

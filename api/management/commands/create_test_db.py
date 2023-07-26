from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Create a PostgreSQL database named "test" for testing'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute('CREATE DATABASE TEST;')
        self.stdout.write(self.style.SUCCESS('Database "test" created successfully.'))

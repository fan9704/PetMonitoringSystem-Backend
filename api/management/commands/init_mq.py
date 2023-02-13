from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        from api.utils.Rabbitmqserver import RabbitmqClient
        try:
            RabbitmqClient.connect()
            RabbitmqClient.channel.queue_declare(queue="hello",durable=False)
        except Exception as E:
            print(E)
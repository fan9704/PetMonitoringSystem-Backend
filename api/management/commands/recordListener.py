from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        from api.utils.Rabbitmqserver import RabbitmqClient
        def callback(ch, method, properties, body:str):
            print("[Consumer] Received ", body.decode(encoding='UTF-8'))
            # print("[Consumer] Done")
            # ch.basic_ack(delivery_tag=method.delivery_tag)

        RabbitmqClient.connect()
        RabbitmqClient.expense("hello",callback)
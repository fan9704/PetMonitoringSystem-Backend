from django.core.management.base import BaseCommand
from PetMonitoringSystemBackend.settings import RABBITMQ_CONFIG
from api.management.commands.callback import recordCallBack, machineCallBack
from api.models import Pet


class Command(BaseCommand):
    def handle(self, *args, **options):
        from api.utils.Rabbitmqserver import RabbitmqServer
        from api.management.commands.callback import recordCallBack, machineCallBack
        if RABBITMQ_CONFIG["enable"]:
            rabbitmqClient = RabbitmqServer(
                username=RABBITMQ_CONFIG["username"],
                password=RABBITMQ_CONFIG["password"],
                serverip=RABBITMQ_CONFIG["serverip"],
                port=RABBITMQ_CONFIG["port"],
                virtual_host=RABBITMQ_CONFIG["vhost"]
            )

        rabbitmqClient.connect()

        # Listen Record
        rabbitmqClient.expense("distance/#", recordCallBack.distanceCallBack)
        rabbitmqClient.expense("temperature/#", recordCallBack.temperatureAndHumidityCallBack)
        rabbitmqClient.expense("weight/#", recordCallBack.weightCallBack)
        rabbitmqClient.expense("water/#", recordCallBack.waterCallBack)
        # Listen Machine
        rabbitmqClient.expense("machine/status/#", machineCallBack.machineCallBack)


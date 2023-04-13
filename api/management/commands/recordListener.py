from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from api.utils.Rabbitmqserver import RabbitmqClient
        from api.management.commands.callback import recordCallBack,machineCallBack

        RabbitmqClient.connect()
        # Listen Record
        RabbitmqClient.expense("distance/#", recordCallBack.distanceCallBack)
        RabbitmqClient.expense("temperature/#", recordCallBack.temperatureAndHumidityCallBack)
        RabbitmqClient.expense("weight/#", recordCallBack.weightCallBack)
        RabbitmqClient.expense("water/#", recordCallBack.waterCallBack)
        # Listen Machine
        RabbitmqClient.expense("machine/status/#", machineCallBack.machineCallBack)

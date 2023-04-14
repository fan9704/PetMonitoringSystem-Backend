# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from api.utils.MQTTserver import mqttClient
        from api.management.commands.callback import recordCallBack, machineCallBack

        # Listen Record
        mqttClient.subscribe_with_callback("distance/#",recordCallBack.distanceCallBack)
        mqttClient.subscribe_with_callback("temperature/#", recordCallBack.temperatureAndHumidityCallBack)
        mqttClient.subscribe_with_callback("weight/#", recordCallBack.weightCallBack)
        mqttClient.subscribe_with_callback("water/#", recordCallBack.waterCallBack)
        # Listen Machine
        mqttClient.subscribe_with_callback("machine/status/#", machineCallBack.machineCallBack)
        # Loop
        mqttClient.loop_forever()


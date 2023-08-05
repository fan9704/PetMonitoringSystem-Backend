# -*- coding:utf-8 -*-
import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from api.utils.MQTTserver import MQTTClient
        from api.management.commands.callback import recordCallBack, machineCallBack
        if os.getenv("RABBITMQ_ENABLE", False):
            mqttClient = MQTTClient(
                broker_host=os.getenv("RABBITMQ_SERVER_IP", "127.0.0.1"),
                broker_port=int(os.getenv("RABBITMQ_PORT", 1883)),
                keepalive=60
            )
            # Listen Record
            mqttClient.subscribe_with_callback("distance/#", recordCallBack.distanceCallBack)
            mqttClient.subscribe_with_callback("temperature/#", recordCallBack.temperatureAndHumidityCallBack)
            mqttClient.subscribe_with_callback("weight/#", recordCallBack.weightCallBack)
            mqttClient.subscribe_with_callback("water/#", recordCallBack.waterCallBack)
            # Listen Machine
            mqttClient.subscribe_with_callback("machine/status/#", machineCallBack.machineCallBack)
            # Loop
            mqttClient.loop_forever()

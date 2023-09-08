# -*- coding:utf-8 -*-
import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from api.utils.MQTTserver import MQTTClient
        from api.management.commands.callback import recordCallBack, machineCallBack
        if os.getenv("RABBITMQ_ENABLE", False):
            mqtt_client = MQTTClient(
                broker_host=os.getenv("RABBITMQ_SERVER_IP", "127.0.0.1"),
                broker_port=int(os.getenv("RABBITMQ_PORT", 1883)),
                keepalive=60
            )
            # Listen Record
            mqtt_client.subscribe_with_callback("distance/#", recordCallBack.distance_callback)
            mqtt_client.subscribe_with_callback("temperature/#", recordCallBack.temperature_humidity_callback)
            mqtt_client.subscribe_with_callback("weight/#", recordCallBack.weight_callback)
            mqtt_client.subscribe_with_callback("water/#", recordCallBack.water_callback)
            # Listen Machine
            mqtt_client.subscribe_with_callback("machine/status/#", machineCallBack.machine_callback)
            # Loop
            mqtt_client.loop_forever()

# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from api.utils.MQTTserver import client

        def on_message(client, userdata, msg):
            print(msg.topic + " " + bytes(msg.payload).decode(encoding='UTF-8'))

        client.on_message = on_message
        client.loop_forever()

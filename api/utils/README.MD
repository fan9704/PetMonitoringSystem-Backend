# RabbitMQ Usage

## AMQP

Use Pika Package

### Util

```python
import logging
import time

import pika

from PetMonitoringSystemBackend.settings import RABBITMQ_CONFIG

logger = logging.getLogger("Rabbitmq Configuration")


class RabbitmqServer(object):
    def __init__(self, username: str, password: str, serverip: str, port: str, virtual_host: str):
        self.channel = None
        self.username = username
        self.password = password
        self.serverip = serverip
        self.port = port
        self.virtual_host = virtual_host

    def connect(self):
        logger.info("Connect to Server")
        user_password = pika.PlainCredentials(self.username, self.password)
        logger.info("Create MQ")
        logger.info("%s,%s,%s,%s,%s" % (self.virtual_host, self.serverip, self.port, self.password, self.username))

        s_conn = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.serverip, port=self.port, credentials=user_password)
        )

        logger.info("Create Channel")
        self.channel = s_conn.channel()
        logger.info("Connect Successful")

    def produce_message(self, queue_name, message):
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.basic_publish(
            exchange="",
            routing_key=queue_name,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2, )  # Message Persist
        )

    def expense(self, queue_name, func):
        self.channel.queue_declare(queue=queue_name, durable=True)  # Optional
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=func,
            auto_ack=True,
        )
        self.channel.start_consuming()


def callback(ch, method, properties, body):
    logger.info("[Consumer] Received %r", body)
    time.sleep(1)
    logger.info("[Consumer] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


if RABBITMQ_CONFIG["enable"]:
    RabbitmqClient = RabbitmqServer(
        username=RABBITMQ_CONFIG["username"],
        password=RABBITMQ_CONFIG["password"],
        serverip=RABBITMQ_CONFIG["serverip"],
        port=RABBITMQ_CONFIG["port"],
        virtual_host=RABBITMQ_CONFIG["vhost"]
    )
RabbitmqClient.connect()
if __name__ == "__main__":
    import json

    data = {"code": 3}
    RabbitmqClient.produce_message("hello", json.dumps(data))
    RabbitmqClient.expense("hello", callback)
```

### RecordListener

```python
from django.core.management.base import BaseCommand
from PetMonitoringSystemBackend.settings import RABBITMQ_CONFIG


class Command(BaseCommand):
    def handle(self, *args, **options):
        from api.utils.Rabbitmqserver import RabbitmqServer
        from api.management.commands.callback import recordCallBack,machineCallBack
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

```

---

## MQTT

```python
import paho.mqtt.client as mqtt
from PetMonitoringSystemBackend.settings import RABBITMQ_CONFIG
import logging

logger = logging.getLogger(__name__)


class MQTTClient:
    def __init__(self, broker_host, broker_port, keepalive=60):
        self.client = mqtt.Client("PetMonitoringBackend")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.callbacks = {}
        self.client.connect(broker_host, broker_port, keepalive)

    def on_connect(self, client, userdata, flags, rc):
        logger.info("Connected with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        if msg.topic.split("/")[0] in self.callbacks:
            self.callbacks[msg.topic.split("/")[0]](
                topic=msg.topic,
                body=msg.payload.decode()
            )

    def set_callback(self, topic, callback):
        self.callbacks[topic.split("/")[0]] = callback

    def subscribe(self, topic):
        logger.info(f"[Subscribe Topic] {topic}")
        self.client.subscribe(topic)

    def subscribe_with_callback(self, topic, callback):
        self.set_callback(topic, callback)
        self.subscribe(topic)

    def loop_forever(self):
        self.client.loop_forever()


if RABBITMQ_CONFIG["enable"]:
    mqttClient = MQTTClient(
        broker_host=RABBITMQ_CONFIG["serverip"],
        broker_port=int(RABBITMQ_CONFIG["port"]),
        keepalive=60
    )

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("weightTopic")


# The callback for when a publish message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


if RABBITMQ_CONFIG["enable"]:
    client = mqtt.Client("PetMonitoringBackend")
    client.on_connect = on_connect
    client.username_pw_set(
        username=RABBITMQ_CONFIG["username"]
        , password=RABBITMQ_CONFIG["password"]
    )
    client.connect(
        RABBITMQ_CONFIG["serverip"],
        RABBITMQ_CONFIG["port"],
        60
    )

```
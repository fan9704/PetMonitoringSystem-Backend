import paho.mqtt.client as mqtt
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
        logger.info(f'Client {client} User Data {userdata} Flags {flags}')

    def on_message(self, client, userdata, msg):
        if msg.topic.split("/")[0] in self.callbacks:
            self.callbacks[msg.topic.split("/")[0]](
                topic=msg.topic,
                body=msg.payload.decode()
            )
        logger.info(f'Client {client} User Data {userdata}')

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

    def loop_stop(self):
        self.client.loop_stop()
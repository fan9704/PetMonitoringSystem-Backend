import paho.mqtt.client as mqtt
from PetMonitoringSystemBackend.settings import RABBITMQ_CONFIG


class MQTTClient:
    def __init__(self, broker_host, broker_port, keepalive=60):
        self.client = mqtt.Client("PetMonitoringBackend")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.callbacks = {}
        self.client.connect(broker_host, broker_port, keepalive)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        if msg.topic in self.callbacks:
            self.callbacks[msg.topic](msg.topic, msg.payload.decode())

    def set_callback(self, topic, callback):
        self.callbacks[topic] = callback

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def subscribe_with_callback(self, topic, callback):
        self.set_callback(topic, callback)
        self.subscribe(topic)

    def loop_forever(self):
        self.client.loop_forever()


if RABBITMQ_CONFIG["enable"]:
    mqttClient = MQTTClient(
        broker_host=RABBITMQ_CONFIG["serverip"],
        broker_port=RABBITMQ_CONFIG["port"],
        keepalive=60
    )

# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code " + str(rc))
#     client.subscribe("weightTopic")
#
#
# # The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     print(msg.topic + " " + str(msg.payload))
#
#
# if RABBITMQ_CONFIG["enable"]:
#     client = mqtt.Client("PetMonitoringBackend")
#     client.on_connect = on_connect
#     client.username_pw_set(
#         username=RABBITMQ_CONFIG["username"]
#         , password=RABBITMQ_CONFIG["password"]
#     )
#     client.connect(
#         RABBITMQ_CONFIG["serverip"],
#         RABBITMQ_CONFIG["port"],
#         60
#     )

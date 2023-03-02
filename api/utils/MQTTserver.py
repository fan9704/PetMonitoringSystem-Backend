import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
from PetMonitoringSystemBackend.settings import RABBITMQ_CONFIG


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("weightTopic")


# The callback for when a PUBLISH message is received from the server.
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
        1883,
        60
    )



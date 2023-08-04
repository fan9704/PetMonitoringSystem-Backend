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

import os
import logging

from django.test import TestCase
from unittest.mock import Mock, patch
from api.utils.MQTTserver import MQTTClient

logger = logging.getLogger(__name__)


class MQTTClientTestCase(TestCase):
    test_topic = 'test/topic'
    host = os.getenv("RABBITMQ_SERVER_IP", "127.0.0.1")
    port = int(os.getenv("RABBITMQ_PORT", 1883))
    mock_mqtt_client = None
    mqtt_client = None

    def setUp(self):
        self.mock_mqtt_client = Mock()
        self.mock_mqtt_client.connect.return_value = None
        self.mock_mqtt_client.loop_forever.return_value = None
        self.mqtt_client = MQTTClient(broker_host=self.host, broker_port=self.port)
        self.mqtt_client.client = self.mock_mqtt_client

        logger.info("Initialize Mock")

    def test_on_connect(self):
        self.mqtt_client.on_connect(self.mock_mqtt_client, None, None, 0)
        self.assertFalse(self.mock_mqtt_client.subscribe.called)
        self.assertEqual(self.mock_mqtt_client.subscribe.call_count, 0)

        logger.info("Complete Test MQTT Connected")

    def test_on_message_with_callback(self):
        mock_callback = Mock()
        self.mqtt_client.set_callback(self.test_topic, mock_callback)
        mock_msg = Mock(topic=self.test_topic, payload=b"Test Payload")
        self.mqtt_client.on_message(self.mock_mqtt_client, None, mock_msg)
        self.assertTrue(mock_callback.called)
        mock_callback.assert_called_once_with(topic=self.test_topic, body="Test Payload")

        logger.info("Complete Test MQTT on message")

    def test_subscribe(self):
        self.mqtt_client.subscribe(self.test_topic)
        self.assertTrue(self.mock_mqtt_client.subscribe.called)
        self.assertEqual(self.mock_mqtt_client.subscribe.call_count, 1)

        logger.info("Complete Test MQTT Subscribe")

    def test_subscribe_with_callback(self):
        mock_callback = Mock()
        self.mqtt_client.subscribe_with_callback(self.test_topic, mock_callback)
        self.assertTrue(self.mock_mqtt_client.subscribe.called)
        self.assertEqual(self.mock_mqtt_client.subscribe.call_count, 1)
        self.assertTrue("test" in self.mqtt_client.callbacks)

        logger.info("Complete Test MQTT Subscribe with callback")

    @patch("paho.mqtt.client.Client.loop_forever")
    def test_loop_forever(self, mock_loop_forever):
        self.mqtt_client.loop_forever()
        self.assertTrue(self.mock_mqtt_client.loop_forever.called)

        logger.info("Complete Test MQTT Loop")

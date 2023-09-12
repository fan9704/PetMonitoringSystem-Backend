import logging

from channels.testing import ChannelsLiveServerTestCase, WebsocketCommunicator

from api.consumers.chatConsumer import ChatConsumer

logger = logging.getLogger(__name__)


class ChatConsumerTests(ChannelsLiveServerTestCase):
    def setUp(self) -> None:
        self.username = "test_user"

    async def connect_to_chat_consumer(self):
        communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), f"/ws/chat/{self.username}/")
        connected, sub_protocol = await communicator.connect()
        logger.info(f"Connected {connected} Sub Protocol {sub_protocol}")
        return communicator

    async def test_connected(self):
        communicator = await self.connect_to_chat_consumer()

        await communicator.disconnect()
        logger.info("Complete Test Connected")

    async def test_chat_consumer(self):
        communicator = await self.connect_to_chat_consumer()

        await communicator.send_json_to({
            "type": "chat.message",
            "message": "Hello from test!"
        })

        response = await communicator.receive_json_from()
        logger.info(response)
        self.assertEqual(response["message"], "Hello from test!")
        self.assertEqual(response["username"], self.username)

        await communicator.disconnect()
        logger.info("Test Chat Consumer")

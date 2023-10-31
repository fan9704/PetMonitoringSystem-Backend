# import logging
#
# from channels.testing import ChannelsLiveServerTestCase, WebsocketCommunicator
#
# from api.consumers.notifyConsumer import NotifyConsumer
#
# logger = logging.getLogger(__name__)
#
#
# class NotifyConsumerTests(ChannelsLiveServerTestCase):
#     async def test_notify_consumer(self):
#         communicator = WebsocketCommunicator(NotifyConsumer.as_asgi(), "/ws/notify/testuser/",
#                                              )
#         connected, sub_protocol = await communicator.connect()
#         logger.info(f"Connected {connected} Sub Protocol {sub_protocol}")
#
#         for i in range(3):
#             response = await communicator.receive_json_from()
#             self.assertIn(f"Message {i + 1}", response["message"])
#
#         await communicator.send_json_to({
#             "type": "chat.message",
#             "message": "Hello from test!"
#         })
#
#         response = await communicator.receive_json_from()
#         logger.info(response)
#         self.assertEqual(response["message"], "Hello, World!")
#         self.assertEqual(response["data"], "Hello from test!")
#
#         await communicator.disconnect()
#         logger.info("Connect Close")
#
#     async def test_load_previous_messages(self):
#         communicator = WebsocketCommunicator(NotifyConsumer.as_asgi(), "/ws/notify/testuser/")
#         connected, sub_protocol = await communicator.connect()
#         logger.info(f"Connected {connected} Sub Protocol {sub_protocol}")
#
#         for i in range(3):
#             response = await communicator.receive_json_from()
#             self.assertIn(f"Message {i + 1}", response["message"])
#
#         await communicator.disconnect()
#         logger.info("Connect Close Loading")
#
#

import logging

from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

logger = logging.getLogger(__name__)


class NotifyConsumer(AsyncJsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None

    async def connect(self):
        self.room_name = self.scope.get('url_route', {}).get('kwargs', {}).get('username')
        self.room_group_name = 'notify_%s' % self.room_name
        logger.info("Connected")
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.loadPreviousMessages()

    async def disconnect(self, close_code):
        logger.info(f"Disconnected {close_code}")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        data = json.loads(text_data)
        logger.info(f"Receive Data {data}")

        response = {
            'message': 'Hello, World!',
            'data': data["message"]
        }
        await self.send(text_data=json.dumps(response))

    async def loadPreviousMessages(self):
        msg_list = ['Message 1', 'Message 2', 'Message 3']
        for message in msg_list:
            await self.send(text_data=json.dumps({
                'message': message
            }))

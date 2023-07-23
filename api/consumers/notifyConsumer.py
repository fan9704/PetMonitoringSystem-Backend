from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json


class NotifyConsumer(AsyncJsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['username']
        self.room_group_name = 'notify_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.loadPreviousMessages()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        data = json.loads(text_data)
        print(data)

        response = {
            'message': 'Hello, World!',
            'data': data["message"]
        }
        # await self.send_json(response)
        await self.channel_layer.group_send(
            self.room_group_name,
            response
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def loadPreviousMessages(self):
        msgList = ['Message 1', 'Message 2', 'Message 3']
        for message in msgList:
            await self.send(text_data=json.dumps({
                'message': message
            }))

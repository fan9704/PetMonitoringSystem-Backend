from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json


class NotifyConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        data = json.loads(text_data)
        print(data)
        if data["message"] == 'PING':
            await self.send('PONG')

        response = {
            'message': 'Hello, World!',
            'data': text_data
        }
        await self.send_json(response)

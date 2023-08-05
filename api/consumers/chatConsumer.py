import json
import os

import openai
from channels.generic.websocket import AsyncWebsocketConsumer


def get_ai_reply(message):
    return f'Hi {message}'
    # openai.api_key = os.getenv("CHATGPT_APIKEY", None)
    # response = openai.Completion.create(
    #     engine="davinci",
    #     prompt=message,
    #     max_tokens=5,
    #     n=1,
    #     stop=None,
    # )
    # return response['choices'][0]['text']


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.username = None

    async def connect(self):
        self.username = self.scope['url_route']['kwargs']['username']
        self.room_name = f'chat_{self.username}'

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': self.username,
        }))

        message = get_ai_reply(message)

        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': 'System',
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))

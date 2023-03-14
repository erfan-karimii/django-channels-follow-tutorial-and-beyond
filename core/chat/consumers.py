import json
import random
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat , ChatRoom

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        print(self.scope['cookies'])
        if self.scope['user'].is_authenticated:
            self.user_name = self.scope['user'].username + " : "
        elif self.scope['cookies']:
            self.user_name = self.scope['cookies']['anonymoususer'] + " : "
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": 'left.','username': self.user_name}
        )
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Find room object
        room = await database_sync_to_async(ChatRoom.objects.get)(name=self.room_name)


        # Creat New Chat
        if self.scope['user'].is_authenticated:
            user = self.scope['user']
        else :
            user = None
        chat = Chat(content= message,user = user,room=room)
        await database_sync_to_async(chat.save)()


        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message,'username': self.user_name}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        if self.user_name == username:
            username = 'ME : '
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message":  username + message}))
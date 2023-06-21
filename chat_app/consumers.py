from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        print("Connected")

    async def disconnect(self, code):
        await self.disconnect(code=code)

    async def send(self, text_data=None, bytes_data=None, close=False):
        await self.send(text_data=text_data, bytes_data=bytes_data, close=close)
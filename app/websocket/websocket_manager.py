class WebSocketManager:

    def __init__(self):
        self.websocket = None
        self.connected = False

    def connect(self, websocket):

        self.websocket = websocket
        self.connected = True

    def disconnect(self):

        self.websocket = None
        self.connected = False

    def is_connected(self):

        return self.connected

    async def send(self, message):

        if self.websocket:

            await self.websocket.send(message)


websocket_manager = WebSocketManager()
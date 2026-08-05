import json
import websockets

from app.websocket.websocket_manager import websocket_manager


class WebSocketClient:

    def __init__(self):

        self.url = None

    async def connect(
        self,
        websocket_url
    ):

        self.url = websocket_url

        print("Connecting to Upstox WebSocket...")

        async with websockets.connect(
            websocket_url
        ) as websocket:

            websocket_manager.connect(
                websocket
            )

            print("✅ WebSocket Connected")

            while True:

                message = await websocket.recv()

                print(
                    json.loads(message)
                )


websocket_client = WebSocketClient()
class WebSocketListener:

    def on_connect(self):
        print("✅ WebSocket Connected")

    def on_disconnect(self):
        print("❌ WebSocket Disconnected")

    def on_message(self, message):
        pass


listener = WebSocketListener()
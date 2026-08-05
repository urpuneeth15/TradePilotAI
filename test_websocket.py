from app.config.settings import settings
from app.websocket.upstox_websocket import UpstoxWebSocket

client = UpstoxWebSocket(settings.UPSTOX_ACCESS_TOKEN)

client.start()
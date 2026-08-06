"""
TradePilot AI
Application Constants
"""


class AppConstants:
    APP_NAME = "TradePilot AI"
    VERSION = "2.0.0"

    REFRESH_INTERVAL = 2

    DEFAULT_CONFIDENCE = 50


class MarketConstants:
    NIFTY = "NSE_INDEX|Nifty 50"
    BANK_NIFTY = "NSE_INDEX|Nifty Bank"

    LIVE = "LIVE"

    BULLISH = "Bullish"
    BEARISH = "Bearish"
    SIDEWAYS = "Sideways"


class SignalConstants:
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


class BrokerConstants:
    UPSTOX = "Upstox"
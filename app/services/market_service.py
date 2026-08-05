from app.brokers.broker_manager import BrokerManager


class MarketService:

    # Instrument keys used for API requests
    NIFTY_KEY = "NSE_INDEX|Nifty 50"
    BANKNIFTY_KEY = "NSE_INDEX|Nifty Bank"

    def _format_quote(self, instrument_key, display_name):

        response = BrokerManager.current().get_market_quote(
    instrument_key
)
        data = response.get("data", {})

        # Upstox returns ":" in the response key instead of "|"
        response_key = instrument_key.replace("|", ":")

        quote = data.get(response_key, {})

        ohlc = quote.get("ohlc", {})

        ltp = quote.get("last_price", 0)
        open_price = ohlc.get("open", 0)
        high = ohlc.get("high", 0)
        low = ohlc.get("low", 0)
        previous_close = ohlc.get("close", 0)
        change = quote.get("net_change", 0)

        signal = "Bullish" if change >= 0 else "Bearish"

        return {
            "symbol": display_name,
            "ltp": ltp,
            "open": open_price,
            "high": high,
            "low": low,
            "previous_close": previous_close,
            "change": change,
            "signal": signal,
            "timestamp": quote.get("timestamp")
        }

    def get_nifty(self):
        return self._format_quote(
            self.NIFTY_KEY,
            "NIFTY 50"
        )

    def get_banknifty(self):
        return self._format_quote(
            self.BANKNIFTY_KEY,
            "BANKNIFTY"
        )
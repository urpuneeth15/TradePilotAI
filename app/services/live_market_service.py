from app.core.market_cache import market_cache


class LiveMarketService:

    def update_quote(
        self,
        instrument_key,
        quote
    ):
        market_cache.update(
            instrument_key,
            quote
        )

    def get_quote(
        self,
        instrument_key
    ):
        # Upstox returns keys with ':' instead of '|'
        cache_key = instrument_key.replace("|", ":")

        return market_cache.get(cache_key)

    def get_all_quotes(self):
        return market_cache.all()

    def clear(self):
        market_cache.clear()

    def has_quote(
        self,
        instrument_key
    ):
        cache_key = instrument_key.replace("|", ":")

        return market_cache.has(cache_key)

        quote = live_market_service.get_quote(
        "NSE_INDEX|Nifty 50"
)

        print("QUOTE:", quote)

        return analysis_service.analyze(
            symbol="NIFTY 50",
            quote=quote
)

live_market_service = LiveMarketService()
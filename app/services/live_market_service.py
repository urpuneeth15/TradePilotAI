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

        key = instrument_key.replace("|", ":")

        return market_cache.get(key)

    def get_all_quotes(self):

        return market_cache.all()

    def clear(self):

        market_cache.clear()


live_market_service = LiveMarketService()
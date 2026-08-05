from app.brokers.broker_interface import BrokerInterface


class DummyBroker(BrokerInterface):

    def login(self):
        return True

    def get_market_quote(self, instrument_key):
        return {
            "last_price": 25000
        }

    def get_history(
        self,
        instrument_key,
        interval,
        to_date,
        from_date
    ):
        return {
            "data": {
                "candles": []
            }
        }

    def get_historical_candles(
        self,
        instrument_key,
        interval,
        to_date,
        from_date
    ):
        return self.get_history(
            instrument_key,
            interval,
            to_date,
            from_date
        )
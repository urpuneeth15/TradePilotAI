from app.brokers.broker_manager import BrokerManager


class CandleService:

    def get_candles(
        self,
        instrument_key,
        interval,
        to_date,
        from_date
    ):
        return BrokerManager.current().get_historical_candles(
            instrument_key,
            interval,
            to_date,
            from_date
        )


candle_service = CandleService()
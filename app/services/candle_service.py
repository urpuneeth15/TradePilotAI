from app.brokers.broker_manager import BrokerManager
from app.services.candle_parser import candle_parser


class CandleService:

    def get_candles(
        self,
        instrument_key,
        interval,
        to_date,
        from_date
    ):

        response = BrokerManager.current().get_historical_candles(
            instrument_key,
            interval,
            to_date,
            from_date
        )

        return candle_parser.parse(response)


candle_service = CandleService()
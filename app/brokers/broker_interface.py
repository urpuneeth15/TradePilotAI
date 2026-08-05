from abc import ABC, abstractmethod


class BrokerInterface(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def get_market_quote(self, instrument_key):
        pass

    @abstractmethod
    def get_history(
        self,
        instrument_key,
        interval,
        to_date,
        from_date
    ):
        pass

    @abstractmethod
    def get_historical_candles(
        self,
        instrument_key,
        interval,
        to_date,
        from_date
    ):
        pass
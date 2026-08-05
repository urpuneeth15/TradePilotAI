from threading import Lock


class MarketCache:

    def __init__(self):
        self._lock = Lock()
        self._quotes = {}

    def update(self, instrument_key: str, data: dict):

        with self._lock:
            self._quotes[instrument_key] = data

    def get(self, instrument_key: str):

        with self._lock:
            return self._quotes.get(instrument_key)

    def all(self):

        with self._lock:
            return dict(self._quotes)

    def clear(self):

        with self._lock:
            self._quotes.clear()

    def has(self, instrument_key):

        with self._lock:
            return instrument_key in self._quotes


market_cache = MarketCache()
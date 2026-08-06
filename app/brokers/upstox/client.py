import requests

from app.auth.token_manager import token_manager
from app.brokers.broker_interface import BrokerInterface


class UpstoxClient(BrokerInterface):

    BASE_URL = "https://api.upstox.com/v2"

    def _headers(self):

        access_token = token_manager.load()

        if not access_token:
            raise Exception(
                "No Upstox access token found. Please login at /auth/login"
            )

        return {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json"
        }

    def login(self):
        return True

    def get_market_quote(self, instrument_key):

        url = (
            f"{self.BASE_URL}/market-quote/quotes"
            f"?instrument_key={instrument_key}"
        )

        response = requests.get(
            url,
            headers=self._headers(),
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    def get_history(
        self,
        instrument_key,
        interval,
        to_date,
        from_date
    ):

        url = (
            f"{self.BASE_URL}/historical-candle/"
            f"{instrument_key}/"
            f"{interval}/"
            f"{to_date}/"
            f"{from_date}"
        )

        response = requests.get(
            url,
            headers=self._headers(),
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    def get_historical_candles(
        self,
        instrument_key,
        interval,
        to_date,
        from_date
    ):

        return self.get_history(
            instrument_key=instrument_key,
            interval=interval,
            to_date=to_date,
            from_date=from_date
        )


upstox_client = UpstoxClient()
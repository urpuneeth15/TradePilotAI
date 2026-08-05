from app.brokers.upstox.client import upstox_client


class BrokerManager:

    @staticmethod
    def current():
        return upstox_client
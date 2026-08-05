import threading
import time

from app.brokers.broker_manager import BrokerManager
from app.services.live_market_service import live_market_service
from app.core.logger import logger


class MarketPoller:

    INSTRUMENTS = [
        "NSE_INDEX|Nifty 50",
        "NSE_INDEX|Nifty Bank"
    ]

    def __init__(self):
        self.running = False

    def start(self):

        if self.running:
            logger.warning("Market Poller is already running.")
            return

        self.running = True

        threading.Thread(
            target=self._poll,
            daemon=True
        ).start()

        logger.info("✅ Market Poller Started")

    def stop(self):

        self.running = False
        logger.info("🛑 Market Poller Stopped")

    def _poll(self):

        broker = BrokerManager.current()

        logger.info("Polling thread started.")

        while self.running:

            for instrument in self.INSTRUMENTS:

                try:

                    response = broker.get_market_quote(instrument)

                    data = response.get("data", {})

                    if not data:
                        logger.warning(
                            f"No market data received for {instrument}"
                        )
                        continue

                    for key, quote in data.items():

                        live_market_service.update_quote(
                            key,
                            quote
                        )

                except Exception as e:

                    logger.error(
                        f"Polling Error ({instrument}): {e}"
                    )

            time.sleep(2)


market_poller = MarketPoller()
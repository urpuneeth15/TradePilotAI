import logging


def setup_logger():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    return logging.getLogger("TradePilotAI")


logger = setup_logger()
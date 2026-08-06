from app.indicators.ema import ema_indicator


class MACDIndicator:

    @staticmethod
    def calculate(prices):

        if len(prices) < 26:
            return None

        ema12 = ema_indicator.calculate(prices, 12)
        ema26 = ema_indicator.calculate(prices, 26)

        if ema12 is None or ema26 is None:
            return None

        macd = ema12 - ema26

        return {
            "macd": round(macd, 2),
            "signal": None,
            "histogram": None
        }


macd_indicator = MACDIndicator()
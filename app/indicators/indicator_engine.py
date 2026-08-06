from app.indicators.ema import ema_indicator
from app.indicators.rsi import rsi_indicator
from app.indicators.macd import macd_indicator


class IndicatorEngine:

    def analyze(self, candles):

        closes = [
            candle["close"]
            for candle in candles
        ]

        ema20 = ema_indicator.calculate(closes, 20)
        ema50 = ema_indicator.calculate(closes, 50)

        rsi = rsi_indicator.calculate(closes)

        macd = macd_indicator.calculate(closes)

        trend = "Bullish"

        if (
            ema20 is not None
            and ema50 is not None
            and ema20 < ema50
        ):
            trend = "Bearish"

        return {

            "ema20": ema20,

            "ema50": ema50,

            "rsi": rsi,

            "macd": macd,

            "trend": trend

        }


indicator_engine = IndicatorEngine()
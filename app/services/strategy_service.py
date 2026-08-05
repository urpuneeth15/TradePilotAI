import pandas as pd

from app.brokers.broker_manager import BrokerManager
from app.utils.date_utils import DateUtils

from app.strategy.indicators import Indicators
from app.strategy.ema_strategy import EMAStrategy
from app.strategy.rsi_strategy import RSIStrategy
from app.strategy.macd_strategy import MACDStrategy
from app.strategy.signal_engine import SignalEngine
from app.strategy.trend import Trend
from app.strategy.confidence_engine import ConfidenceEngine
from app.strategy.option_engine import OptionEngine


class StrategyService:

    NIFTY_KEY = "NSE_INDEX|Nifty 50"

    def get_signal(self):

        # Fetch historical candles
        response = BrokerManager.current().get_history(
            instrument_key=self.NIFTY_KEY,
            interval="day",
            from_date=DateUtils.days_before(60),
            to_date=DateUtils.today()
        )

        candles = response["data"]["candles"]

        # Create DataFrame
        df = pd.DataFrame(
            candles,
            columns=[
                "timestamp",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "oi"
            ]
        )

        # Upstox returns newest candle first
        df = df.iloc[::-1].reset_index(drop=True)

        # Calculate Indicators
        df = Indicators.ema(df)
        df = Indicators.rsi(df)
        df = Indicators.macd(df)

        latest = df.iloc[-1]

        # Individual Signals
        ema_signal = EMAStrategy.signal(df)

        rsi_signal = RSIStrategy.signal(
            latest["RSI"]
        )

        macd_signal = MACDStrategy.signal(
            latest["MACD"],
            latest["Signal"]
        )

        # Final AI Signal
        final_signal = SignalEngine.decide(
            ema_signal,
            rsi_signal,
            macd_signal
        )

        # Trend
        trend = Trend.market(df)

        # Confidence
        confidence = ConfidenceEngine.calculate(
            ema=ema_signal,
            rsi=rsi_signal,
            macd=macd_signal,
            trend=trend,
            final_signal=final_signal.signal
        )

        # Trade Recommendation
        trade = OptionEngine.recommend(
            signal=final_signal.signal,
            nifty_price=float(latest["close"]),
            confidence=confidence
        )

        return {
            "market": "NIFTY 50",
            "price": round(float(latest["close"]), 2),
            "trend": trend,
            "signal": final_signal.signal,
            "confidence": confidence,
            "indicators": {
                "EMA": ema_signal,
                "RSI": rsi_signal,
                "MACD": macd_signal
            },
            "trade": trade,
            "reason": final_signal.reason,
            "values": {
                "EMA20": round(float(latest["EMA_20"]), 2),
                "RSI": round(float(latest["RSI"]), 2),
                "MACD": round(float(latest["MACD"]), 2),
                "MACD_SIGNAL": round(float(latest["Signal"]), 2)
            }
        }
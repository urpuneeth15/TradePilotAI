from app.indicators.indicator_engine import indicator_engine
from app.strategy.signal_engine import signal_engine
from app.strategy.confidence_engine import confidence_engine


class AIEngine:

    def analyze(self, candles):

        indicators = indicator_engine.analyze(
            candles
        )

        signal_data = signal_engine.generate(
            indicators
        )

        confidence = confidence_engine.calculate(
            signal_data["bullish_score"],
            signal_data["bearish_score"]
        )

        return {

            "trend": indicators["trend"],

            "signal": signal_data["signal"],

            "confidence": confidence,

            "reasons": signal_data["reasons"],

            "indicators": indicators

        }


ai_engine = AIEngine()
from datetime import datetime

from app.indicators.indicator_engine import indicator_engine
from app.strategy.signal_engine import signal_engine
from app.strategy.confidence_engine import confidence_engine


class AnalysisService:

    def analyze(
        self,
        symbol: str,
        quote: dict,
        candles: list | None = None
    ):

        if not quote:

            return {
                "symbol": symbol,
                "status": "No Data"
            }

        # -----------------------------
        # Live Market Data
        # -----------------------------

        ltp = quote.get("last_price", 0)

        change = quote.get("net_change", 0)

        previous_close = (
            quote.get("ohlc", {})
            .get("close", 0)
        )

        if previous_close:

            change_percent = round(
                (change / previous_close) * 100,
                2
            )

        else:

            change_percent = 0

        # -----------------------------
        # Default Values
        # -----------------------------

        trend = "Sideways"

        signal = "WAIT"

        confidence = 50

        indicators = None

        reasons = []

        # -----------------------------
        # AI Indicator Analysis
        # -----------------------------

        if candles:

            indicators = indicator_engine.analyze(
                candles
            )

            trend = indicators.get(
                "trend",
                "Sideways"
            )

            signal_data = signal_engine.generate(
                indicators
            )

            signal = signal_data["signal"]

            confidence = confidence_engine.calculate(
                signal_data["bullish_score"],
                signal_data["bearish_score"]
            )

            reasons = signal_data["reasons"]

        else:

            # Fallback if candles are unavailable

            if change > 0:

                trend = "Bullish"

                signal = "BUY"

                confidence = 70

                reasons = [
                    "Positive price movement"
                ]

            elif change < 0:

                trend = "Bearish"

                signal = "SELL"

                confidence = 70

                reasons = [
                    "Negative price movement"
                ]

            else:

                trend = "Sideways"

                signal = "WAIT"

                confidence = 50

                reasons = [
                    "No significant movement"
                ]

        return {

            "symbol": symbol,

            "ltp": round(ltp, 2),

            "change": round(change, 2),

            "change_percent": round(
                change_percent,
                2
            ),

            "trend": trend,

            "signal": signal,

            "confidence": confidence,

            "reasons": reasons,

            "last_updated": datetime.now().strftime(
                "%H:%M:%S"
            ),

            "indicators": indicators

        }


analysis_service = AnalysisService()
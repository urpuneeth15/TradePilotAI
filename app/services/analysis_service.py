from datetime import datetime


class AnalysisService:

    def analyze(
        self,
        symbol: str,
        quote: dict
    ):

        if not quote:

            return {
                "symbol": symbol,
                "status": "No Data"
            }

        ltp = quote.get("last_price", 0)

        change = quote.get("net_change", 0)

        previous_close = quote.get("close", 0)

        if previous_close:

            change_percent = round(
                (change / previous_close) * 100,
                2
            )

        else:

            change_percent = 0

        if change > 0:

            trend = "Bullish"

            signal = "BUY"

            confidence = min(
                95,
                70 + abs(change_percent) * 5
            )

        elif change < 0:

            trend = "Bearish"

            signal = "SELL"

            confidence = min(
                95,
                70 + abs(change_percent) * 5
            )

        else:

            trend = "Sideways"

            signal = "HOLD"

            confidence = 50

        return {

            "symbol": symbol,

            "ltp": round(ltp, 2),

            "change": round(change, 2),

            "change_percent": round(change_percent, 2),

            "trend": trend,

            "signal": signal,

            "confidence": round(confidence),

            "last_updated": datetime.now().strftime(
                "%H:%M:%S"
            )

        }


analysis_service = AnalysisService()
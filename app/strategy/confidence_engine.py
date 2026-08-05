class ConfidenceEngine:

    WEIGHTS = {
        "EMA": 35,
        "RSI": 20,
        "MACD": 25,
        "TREND": 20
    }

    @staticmethod
    def calculate(ema, rsi, macd, trend, final_signal):

        score = 0

        if ema == final_signal:
            score += ConfidenceEngine.WEIGHTS["EMA"]

        if rsi == final_signal:
            score += ConfidenceEngine.WEIGHTS["RSI"]

        if macd == final_signal:
            score += ConfidenceEngine.WEIGHTS["MACD"]

        trend_signal = "BUY" if trend == "Bullish" else "SELL"

        if trend_signal == final_signal:
            score += ConfidenceEngine.WEIGHTS["TREND"]

        return score
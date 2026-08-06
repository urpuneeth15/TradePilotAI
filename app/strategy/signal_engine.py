class SignalEngine:

    def generate(self, indicators):

        bullish = 0
        bearish = 0
        reasons = []

        ema20 = indicators.get("ema20")
        ema50 = indicators.get("ema50")
        rsi = indicators.get("rsi")
        macd = indicators.get("macd")

        # EMA
        if ema20 is not None and ema50 is not None:

            if ema20 > ema50:
                bullish += 2
                reasons.append("EMA20 above EMA50")

            elif ema20 < ema50:
                bearish += 2
                reasons.append("EMA20 below EMA50")

        # RSI

        if rsi is not None:

            if rsi < 30:
                bullish += 2
                reasons.append("RSI Oversold")

            elif rsi > 70:
                bearish += 2
                reasons.append("RSI Overbought")

            else:
                bullish += 1
                reasons.append("RSI Neutral")

        # MACD

        if macd:

            value = macd.get("macd", 0)

            if value > 0:
                bullish += 2
                reasons.append("MACD Bullish")

            else:
                bearish += 2
                reasons.append("MACD Bearish")

        # Final Decision

        if bullish >= 5:
            signal = "STRONG BUY"

        elif bullish > bearish:
            signal = "BUY"

        elif bearish >= 5:
            signal = "STRONG SELL"

        elif bearish > bullish:
            signal = "SELL"

        else:
            signal = "WAIT"

        return {

            "signal": signal,

            "bullish_score": bullish,

            "bearish_score": bearish,

            "reasons": reasons

        }


signal_engine = SignalEngine()
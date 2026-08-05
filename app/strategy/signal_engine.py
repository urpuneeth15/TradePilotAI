from app.models.signal import Signal


class SignalEngine:

    @staticmethod
    def decide(
        ema_signal,
        rsi_signal,
        macd_signal
    ):

        votes = [ema_signal, rsi_signal, macd_signal]

        buy = votes.count("BUY")
        sell = votes.count("SELL")

        if buy > sell:

            return Signal(
                signal="BUY",
                confidence=buy * 33,
                ema=ema_signal,
                rsi=rsi_signal,
                macd=macd_signal,
                reason=[
                    "Majority indicators are bullish"
                ]
            )

        if sell > buy:

            return Signal(
                signal="SELL",
                confidence=sell * 33,
                ema=ema_signal,
                rsi=rsi_signal,
                macd=macd_signal,
                reason=[
                    "Majority indicators are bearish"
                ]
            )

        return Signal(
            signal="HOLD",
            confidence=50,
            ema=ema_signal,
            rsi=rsi_signal,
            macd=macd_signal,
            reason=[
                "Indicators are mixed"
            ]
        )
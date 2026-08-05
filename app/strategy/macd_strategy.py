class MACDStrategy:

    @staticmethod
    def signal(macd, signal):

        if macd > signal:
            return "BUY"

        elif macd < signal:
            return "SELL"

        return "HOLD"
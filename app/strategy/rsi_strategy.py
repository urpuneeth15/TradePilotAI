class RSIStrategy:

    @staticmethod
    def signal(rsi):

        if rsi > 60:
            return "BUY"

        elif rsi < 40:
            return "SELL"

        return "HOLD"
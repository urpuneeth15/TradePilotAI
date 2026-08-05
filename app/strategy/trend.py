class Trend:

    @staticmethod
    def market(df):

        latest = df.iloc[-1]

        ema = latest["EMA_20"]

        price = latest["close"]

        if price > ema:
            return "Bullish"

        elif price < ema:
            return "Bearish"

        return "Sideways"
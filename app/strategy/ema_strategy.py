import pandas as pd


class EMAStrategy:

    @staticmethod
    def calculate(df, period=20):

        df[f"EMA_{period}"] = (
            df["close"]
            .ewm(span=period, adjust=False)
            .mean()
        )

        return df

    @staticmethod
    def signal(df):

        latest = df.iloc[-1]

        if latest["close"] > latest["EMA_20"]:
            return "BUY"

        elif latest["close"] < latest["EMA_20"]:
            return "SELL"

        return "HOLD"
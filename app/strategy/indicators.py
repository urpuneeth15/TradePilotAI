import pandas as pd


class Indicators:

    @staticmethod
    def ema(df, period=20):

        df[f"EMA_{period}"] = (
            df["close"]
            .ewm(span=period, adjust=False)
            .mean()
        )

        return df

    @staticmethod
    def rsi(df, period=14):

        delta = df["close"].diff()

        gain = delta.clip(lower=0)

        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(period).mean()

        avg_loss = loss.rolling(period).mean()

        rs = avg_gain / avg_loss

        df["RSI"] = 100 - (100 / (1 + rs))

        return df

    @staticmethod
    def macd(df):

        ema12 = df["close"].ewm(span=12).mean()

        ema26 = df["close"].ewm(span=26).mean()

        df["MACD"] = ema12 - ema26

        df["Signal"] = df["MACD"].ewm(span=9).mean()

        return df
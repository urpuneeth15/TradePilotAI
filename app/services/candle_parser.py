class CandleParser:

    @staticmethod
    def parse(response: dict):

        candles = []

        data = response.get("data", [])

        if isinstance(data, dict):

            data = data.get("candles", [])

        for candle in data:

            try:

                candles.append(
                    {
                        "time": candle[0],
                        "open": float(candle[1]),
                        "high": float(candle[2]),
                        "low": float(candle[3]),
                        "close": float(candle[4]),
                        "volume": float(candle[5]) if len(candle) > 5 else 0
                    }
                )

            except Exception:
                continue

        return candles


candle_parser = CandleParser()
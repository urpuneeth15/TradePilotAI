from typing import List


class RSIIndicator:

    @staticmethod
    def calculate(prices: List[float], period: int = 14):

        if len(prices) <= period:
            return None

        gains = []
        losses = []

        for i in range(1, len(prices)):

            change = prices[i] - prices[i - 1]

            gains.append(max(change, 0))
            losses.append(abs(min(change, 0)))

        avg_gain = sum(gains[:period]) / period
        avg_loss = sum(losses[:period]) / period

        if avg_loss == 0:
            return 100

        rs = avg_gain / avg_loss

        rsi = 100 - (100 / (1 + rs))

        return round(rsi, 2)


rsi_indicator = RSIIndicator()
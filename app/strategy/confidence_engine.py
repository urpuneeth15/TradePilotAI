class ConfidenceEngine:

    def calculate(self, bullish, bearish):

        score = max(bullish, bearish)

        confidence = min(
            95,
            50 + (score * 10)
        )

        return confidence


confidence_engine = ConfidenceEngine()
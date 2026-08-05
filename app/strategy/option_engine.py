from datetime import datetime


class OptionEngine:

    @staticmethod
    def nearest_strike(price):
        return round(price / 50) * 50

    @staticmethod
    def expiry_type():
        # Placeholder
        # Later we'll calculate the actual expiry date
        return "Weekly"

    @staticmethod
    def recommend(signal, nifty_price, confidence):

        strike = OptionEngine.nearest_strike(nifty_price)

        trade = {
            "option_type": "NONE",
            "strike_type": "ATM",
            "strike": strike,
            "expiry": OptionEngine.expiry_type(),
            "entry": round(nifty_price, 2),
            "stop_loss": 0,
            "target_1": 0,
            "target_2": 0,
            "confidence": confidence
        }

        if signal == "BUY":
            trade["option_type"] = "CALL"
            trade["stop_loss"] = round(nifty_price - 40, 2)
            trade["target_1"] = round(nifty_price + 60, 2)
            trade["target_2"] = round(nifty_price + 120, 2)

        elif signal == "SELL":
            trade["option_type"] = "PUT"
            trade["stop_loss"] = round(nifty_price + 40, 2)
            trade["target_1"] = round(nifty_price - 60, 2)
            trade["target_2"] = round(nifty_price - 120, 2)

        return trade
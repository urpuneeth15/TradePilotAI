class RiskEngine:

    @staticmethod
    def calculate(
        capital,
        entry,
        stop_loss,
        lot_size=75,
        risk_percent=1
    ):

        max_risk = capital * (risk_percent / 100)

        risk_per_lot = abs(entry - stop_loss) * lot_size

        quantity = max(
            1,
            int(max_risk // risk_per_lot)
        )

        expected_profit = quantity * abs(entry - stop_loss) * 2

        return {
            "capital": capital,
            "risk_per_trade": round(max_risk, 2),
            "lots": quantity,
            "max_loss": round(risk_per_lot * quantity, 2),
            "expected_profit": round(expected_profit, 2)
        }
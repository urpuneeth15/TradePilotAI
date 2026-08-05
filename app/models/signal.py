from dataclasses import dataclass


@dataclass
class Signal:

    signal: str

    confidence: int

    ema: str

    rsi: str

    macd: str

    reason: list
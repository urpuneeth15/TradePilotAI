from dataclasses import dataclass


@dataclass
class Trade:

    signal: str

    option_type: str

    strike: int

    entry: float

    stop_loss: float

    target_1: float

    target_2: float

    confidence: int
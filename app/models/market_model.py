from pydantic import BaseModel


class MarketAnalysis(BaseModel):

    symbol: str

    ltp: float

    change: float

    change_percent: float

    trend: str

    signal: str

    confidence: int

    last_updated: str
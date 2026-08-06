from fastapi import APIRouter
from datetime import datetime, timedelta

from app.services.live_market_service import live_market_service
from app.services.candle_service import candle_service
from app.services.analysis_service import analysis_service

router = APIRouter(tags=["AI Analysis"])


@router.get("/analysis")
def analysis():

    quote = live_market_service.get_quote(
        "NSE_INDEX|Nifty 50"
    )

    to_date = datetime.today().strftime("%Y-%m-%d")

    from_date = (
        datetime.today() - timedelta(days=120)
    ).strftime("%Y-%m-%d")

    candles = candle_service.get_candles(
        instrument_key="NSE_INDEX|Nifty 50",
        interval="day",
        to_date=to_date,
        from_date=from_date
    )

    return analysis_service.analyze(
        symbol="NIFTY 50",
        quote=quote,
        candles=candles
    )
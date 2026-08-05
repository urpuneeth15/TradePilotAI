from fastapi import APIRouter, Query
from datetime import datetime, timedelta

from app.services.candle_service import candle_service

router = APIRouter(tags=["Candles"])


@router.get("/history")
def history(
    interval: str = Query("day"),
    days: int = Query(30, ge=1, le=365)
):

    to_date = datetime.today().strftime("%Y-%m-%d")
    from_date = (
        datetime.today() - timedelta(days=days)
    ).strftime("%Y-%m-%d")

    return candle_service.get_candles(
        instrument_key="NSE_INDEX|Nifty 50",
        interval=interval,
        to_date=to_date,
        from_date=from_date
    )
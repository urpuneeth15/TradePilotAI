from fastapi import APIRouter

from app.services.live_market_service import live_market_service

router = APIRouter()


@router.get("/live")
def all_quotes():

    return live_market_service.get_all_quotes()


@router.get("/live/nifty")
def nifty():

    return live_market_service.get_quote(
        "NSE_INDEX|Nifty 50"
    )


@router.get("/live/banknifty")
def banknifty():

    return live_market_service.get_quote(
        "NSE_INDEX|Nifty Bank"
    )
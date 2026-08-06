from fastapi import APIRouter

from app.services.live_market_service import live_market_service
from app.services.analysis_service import analysis_service

router = APIRouter()


@router.get("/live")
def all_quotes():

    quotes = live_market_service.get_all_quotes()

    result = {}

    for instrument, quote in quotes.items():

        symbol = instrument.replace(":", "|")

        result[instrument] = analysis_service.analyze(
            symbol=symbol,
            quote=quote
        )

    return result


@router.get("/live/nifty")
def nifty():

    quote = live_market_service.get_quote(
        "NSE_INDEX|Nifty 50"
    )

    return analysis_service.analyze(
        symbol="NIFTY 50",
        quote=quote
    )


@router.get("/live/banknifty")
def banknifty():

    quote = live_market_service.get_quote(
        "NSE_INDEX|Nifty Bank"
    )

    return analysis_service.analyze(
        symbol="BANK NIFTY",
        quote=quote
    )
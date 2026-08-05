from fastapi import APIRouter
from app.services.market_service import MarketService
from app.services.strategy_service import StrategyService

strategy_service = StrategyService()

router = APIRouter(tags=["Market"])

market_service = MarketService()

@router.get("/nifty")
def get_nifty():
    return market_service.get_nifty()

@router.get("/banknifty")
def get_banknifty():
    return market_service.get_banknifty()

@router.get("/signal")
def get_signal():
    return strategy_service.get_signal()
from fastapi import APIRouter
from datetime import datetime

from app.config.settings import settings
from app.core.market_cache import market_cache
from app.services.market_poller import market_poller

router = APIRouter(tags=["Status"])

START_TIME = datetime.now()


@router.get("/status")
def get_status():

    uptime = datetime.now() - START_TIME

    cache = market_cache.all()

    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION,
        "server": "Running",
        "broker": "Upstox",
        "market_source": "REST Poller",
        "poller_running": market_poller.running,
        "cache_size": len(cache),
        "cached_instruments": list(cache.keys()),
        "uptime": str(uptime).split(".")[0]
    }
from fastapi import FastAPI

from app.config.settings import settings

from app.market.market_data import router as market_router
from app.market.candle_data import router as candle_router
from app.auth.upstox_auth import router as auth_router
from app.market.live_market import router as live_market_router
from app.routers.status import router as status_router
from app.core.request_logger import RequestLoggerMiddleware
from app.core.exception_handler import register_exception_handlers
from app.core.logger import logger

from app.services.market_poller import market_poller

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

register_exception_handlers(app)

app.add_middleware(
    RequestLoggerMiddleware
)

@app.on_event("startup")
def startup():

    logger.info("===================================")
    logger.info("TradePilot AI Backend Starting...")
    logger.info(f"Version : {settings.VERSION}")

    market_poller.start()

    logger.info("Backend Started Successfully")
    logger.info("===================================")


@app.get("/")
def home():

    return {
        "message": "Welcome to TradePilot AI",
        "status": "Running"
    }


@app.get("/health")
def health():

    return {
        "server": "Healthy",
        "version": settings.VERSION
    }


# Market Routes
app.include_router(
    market_router,
    prefix="/market"
)

app.include_router(
    candle_router,
    prefix="/market"
)

app.include_router(
    live_market_router,
    prefix="/market"
)

# Authentication
app.include_router(
    auth_router,
    prefix="/auth"
)

# Status
app.include_router(
    status_router
)
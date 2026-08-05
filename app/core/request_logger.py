from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import logger


class RequestLoggerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        logger.info(
            f"{request.method} {request.url.path}"
        )

        response = await call_next(request)

        return response
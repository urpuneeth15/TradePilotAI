from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.logger import logger


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception
    ):

        logger.exception(
            f"Unhandled Exception at {request.url.path}"
        )

        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "An unexpected error occurred"
            }
        )
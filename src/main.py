from contextlib import asynccontextmanager
import logging

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi.exception_handlers import http_exception_handler
from fastapi import FastAPI, HTTPException, Request
from src.logging_conf import configure_logging

from src.routers.movies_router import router as movie_router

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(CorrelationIdMiddleware)

app.include_router(movie_router)

@app.exception_handler(HTTPException)
async def http_exception_handle_logging(request, exc):
    logger.error(f"HTTPException: {exc.status_code} {exc.detail}")
    return await http_exception_handler(request, exc)

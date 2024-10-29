
import logging
from fastapi import APIRouter
from src.services import movie_service


router = APIRouter()

logger = logging.getLogger(__name__)

@router.get("/popular")
async def get_popular():
    return movie_service.get_popular_movies()


import logging
from typing import List
from fastapi import APIRouter
from src.models.movie import Movie
from src.services.movie_service import MovieService


router = APIRouter()

logger = logging.getLogger(__name__)

@router.get("/popular")
async def get_popular() -> List[Movie]:
    service = MovieService()
    return service.get_popular_movies()

@router.get("/search")
async def search_movie(movie_title: str) -> List[Movie]:
    service = MovieService()
    return service.search_movie(movie_title)

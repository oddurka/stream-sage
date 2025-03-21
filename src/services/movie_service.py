import logging
from typing import List

from icecream import ic
import requests
from src.clients.the_movie_db.client import TheMovieDBClient
from src.config import config
from src.models.movie import Movie

logger = logging.getLogger(__name__)

class MovieService:
    def __init__(self):
        self.client = TheMovieDBClient()

    def get_popular_movies(self) -> List[Movie]:
        logger.info("Getting popular movies")
        popular_movies = self.client.get_popular_movies()

        return popular_movies

    def search_movie(self, movie_title: str) -> List[Movie]:
        logger.info(f"Searching for movie: {movie_title}")
        movie = self.client.search_movie(movie_title)

        return movie

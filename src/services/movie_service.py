import logging
from typing import List

import requests
from src.config import config
from src.models.movie import Movie

logger = logging.getLogger(__name__)

class MovieService:
    def _headers(self):
        return {
            "accept": "application/json",
            "Authorization": f"Bearer {config.MOVIEDB_BEARER}",
        }

    def get_popular_movies(self) -> List[Movie]:
        logger.info("Getting popular movies")

        url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
        response = requests.get(url, headers=self._headers())

        popular_movies = [Movie(**movie) for movie in response.json()["results"]]
        return popular_movies

    def search_movie(self, movie_title: str) -> dict:
        logger.info(f"Searching for movie: {movie_title}")

        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"
        response = requests.get(url, headers=self._headers())

        return response.json()

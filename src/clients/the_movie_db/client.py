from typing import List
import requests
from src.clients.the_movie_db.models import TMDBMovie
from src.config import config
from icecream import ic


class TheMovieDBClient:
    def __init__(self):
        self.base_url = "https://api.themoviedb.org/3"

    def _headers(self):
        return {
            "accept": "application/json",
            "Authorization": f"Bearer {config.MOVIEDB_BEARER}",
        }

    def get_popular_movies(self) -> List[TMDBMovie]:
        url = f"{self.base_url}/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
        response = requests.get(url, headers=self._headers())
        return [TMDBMovie(**movie) for movie in response.json()["results"]]

    def search_movie(self, movie_title: str) -> List[TMDBMovie]:
        url = f"{self.base_url}/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"
        response = requests.get(url, headers=self._headers())
        return [TMDBMovie(**movie) for movie in response.json()["results"]]


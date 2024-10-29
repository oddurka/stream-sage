
import logging

import requests
from src.config import config

logger = logging.getLogger(__name__)

class MovieService:
    def _headers(self):
        return {
            "accept": "application/json",
            "Authorization": f"Bearer {config.MOVIEDB_BEARER}",
        }

    def get_popular_movies(self):
        logger.info("Getting popular movies")

        url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
        response = requests.get(url, headers=self._headers())

        return response.json()

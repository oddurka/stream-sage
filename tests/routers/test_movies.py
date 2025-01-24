from starlette.testclient import TestClient
from unittest.mock import MagicMock, patch

class TestMovieRouter:
    @patch("src.services.movie_service.requests.get")
    def test_get_popular_movies(self, mock_get, client: TestClient) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {
                    "adult": False,
                    "backdrop_path": "/2siOHQYDG7gCQB6g69g2pTZiSia.jpg",
                    "genre_ids": [10751, 14],
                    "id": 447273,
                    "original_language": "en",
                    "original_title": "Snow White",
                    "overview": "A princess joins forces with seven dwarfs to liberate her kingdom from her cruel stepmother, the Evil Queen.",
                    "popularity": 30.454,
                    "poster_path": "/xWWg47tTfparvjK0WJNX4xL8lW2.jpg",
                    "release_date": "2025-03-19",
                    "title": "Snow White",
                    "video": False,
                    "vote_average": 4.4,
                    "vote_count": 106
                },
            ]
        }
 

        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = client.get("/popular")

        assert response.status_code == 200

    @patch("src.services.movie_service.requests.get")
    def test_search_movie(self, mock_get, client: TestClient) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {"results": [{"title": "Movie 1"}, {"title": "Movie 2"}]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = client.get("/search?movie_title=Movie")
        assert response.status_code == 200

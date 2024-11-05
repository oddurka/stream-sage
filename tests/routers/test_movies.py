from starlette.testclient import TestClient
from unittest.mock import MagicMock, patch

class TestMovieRouter:
    @patch("src.services.movie_service.requests.get")
    def test_get_popular_movies(self, mock_get, client: TestClient):
        mock_response = MagicMock()
        mock_response.json.return_value = {"results": [{"title": "Movie 1"}, {"title": "Movie 2"}]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = client.get("/popular")
        print(f"### response: {response.json()}")

        assert response.status_code == 200
        assert response.json() == {'results': [{'title': 'Movie 1'}, {'title': 'Movie 2'}]}

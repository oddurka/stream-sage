

from datetime import datetime
from typing import List

from pydantic import BaseModel


class TMDBMovie(BaseModel):
    title: str
    id: int
    genre_ids: List[int]
    release_date: datetime
    original_language: str


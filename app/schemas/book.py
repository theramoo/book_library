from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    genre: Optional[str] = None


class BookResponse(BookCreate):
    id: int

    class Config:
        orm_mode = True

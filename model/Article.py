from pydantic import BaseModel

class Article(BaseModel):
    id: int
    name: str
    price: float
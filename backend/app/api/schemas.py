from pydantic import BaseModel


class SearchResult(BaseModel):

    title: str
    score: float
    semantic_score: float
    lexical_score: float
    personalization_score: float

class SearchResponse(BaseModel):

    query: str
    results: list[SearchResult]
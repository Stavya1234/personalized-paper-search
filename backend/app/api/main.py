from fastapi import FastAPI

from backend.app.search.hybrid_search import (
    hybrid_search
)

from backend.app.api.schemas import (
    SearchResponse
)

app = FastAPI(
    title="Personalized Paper Search API"
)


@app.get("/")
def root():

    return {
        "message":
            "Personalized Paper Search API"
    }


@app.get(
    "/search",
    response_model=SearchResponse
)
def search(
    query: str,
    top_k: int = 5
):

    results = hybrid_search(
        query=query,
        top_k=top_k
    )

    return {
        "query": query,
        "results": results
    }
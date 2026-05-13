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
    preferences: str = "",
    top_k: int = 5
):

    user_preferences = [
        pref.strip()
        for pref in preferences.split(",")
        if pref.strip()
    ]

    results = hybrid_search(
        query=query,
        top_k=top_k,
        user_preferences=user_preferences
    )

    return {
        "query": query,
        "results": results
    }
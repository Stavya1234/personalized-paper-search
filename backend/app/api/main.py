from fastapi import FastAPI

from backend.app.search.hybrid_search import hybrid_search

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Personalized Paper Search API"
    }


@app.get("/search")
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
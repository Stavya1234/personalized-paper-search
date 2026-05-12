from rank_bm25 import BM25Okapi

from backend.app.db.database import SessionLocal
from backend.app.db.models import Paper


db = SessionLocal()

papers = db.query(Paper).all()

corpus = [
    f"{paper.title} {paper.abstract}"
    for paper in papers
]

tokenized_corpus = [
    doc.lower().split()
    for doc in corpus
]

bm25 = BM25Okapi(tokenized_corpus)


def lexical_search(query, top_k=5):

    tokenized_query = query.lower().split()

    scores = bm25.get_scores(tokenized_query)

    results = []

    for paper, score in zip(papers, scores):

        results.append({
            "title": paper.title,
            "score": float(score)
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]


if __name__ == "__main__":

    query = input("Search query: ")

    results = lexical_search(query)

    print("\nTop Results:\n")

    for result in results:

        print(
            f"{result['score']:.4f} | "
            f"{result['title']}"
        )
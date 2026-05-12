from sentence_transformers import SentenceTransformer
import numpy as np

from backend.app.db.database import SessionLocal
from backend.app.db.models import Paper

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def semantic_search(query, top_k=5):

    db = SessionLocal()

    query_embedding = model.encode(query)

    papers = db.query(Paper).all()

    results = []

    for paper in papers:

        paper_embedding = np.frombuffer(
            paper.embedding,
            dtype=np.float32
        )

        similarity = np.dot(
            query_embedding,
            paper_embedding
        ) / (
            np.linalg.norm(query_embedding)
            * np.linalg.norm(paper_embedding)
        )

        results.append({
            "title": paper.title,
            "score": float(similarity)
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]

if __name__ == "__main__":
    
    query = input("Search query: ")

    results = semantic_search(query)

    print("\nTop Results:\n")

    for result in results:

        print(
            f"{result['score']:.4f} | "
            f"{result['title']}"
        )
from sentence_transformers import SentenceTransformer
import numpy as np

from backend.app.db.database import SessionLocal
from backend.app.db.models import Paper

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

db = SessionLocal()

query = input("Search query: ")

# Convert user query into semantic vector
query_embedding = model.encode(query)

papers = db.query(Paper).all()

results = []

for paper in papers:

    paper_embedding = np.frombuffer(
        paper.embedding,
        dtype=np.float32
    )

    # Compute cosine similarity
    similarity = np.dot(
        query_embedding,
        paper_embedding
    ) / (
        np.linalg.norm(query_embedding)
        * np.linalg.norm(paper_embedding)
    )

    results.append(
        (similarity, paper.title)
    )

results.sort(reverse=True)

print("\nTop Results:\n")

for score, title in results[:5]:

    print(f"{score:.4f} - {title}")

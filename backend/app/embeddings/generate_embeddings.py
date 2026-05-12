from sentence_transformers import SentenceTransformer
import numpy as np

from backend.app.db.database import SessionLocal
from backend.app.db.models import Paper

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

db = SessionLocal()

papers = db.query(Paper).all()

for paper in papers:

    text = f"{paper.title} {paper.abstract}"

    embedding = model.encode(text)

    paper.embedding = embedding.astype(
        np.float32
    ).tobytes()

db.commit()

print("Embeddings generated.")


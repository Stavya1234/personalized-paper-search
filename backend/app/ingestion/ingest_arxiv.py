import requests
import xml.etree.ElementTree as ET

from backend.app.db.database import SessionLocal, engine
from backend.app.db.models import Base, Paper

Base.metadata.create_all(bind=engine)

db = SessionLocal()

ARXIV_URL = (
    "https://export.arxiv.org/api/query?"
    "search_query=cat:cs.LG"
    "&start=0"
    "&max_results=100"
)

response = requests.get(ARXIV_URL)

root = ET.fromstring(response.text)

namespace = {
    "atom": "http://www.w3.org/2005/Atom"
}

for entry in root.findall("atom:entry", namespace):

    title = entry.find(
        "atom:title",
        namespace
    ).text.strip()

    abstract = entry.find(
        "atom:summary",
        namespace
    ).text.strip()

    published = entry.find(
        "atom:published",
        namespace
    ).text.strip()

    paper_id = entry.find(
        "atom:id",
        namespace
    ).text.strip()

    authors = []

    for author in entry.findall(
        "atom:author",
        namespace
    ):
        name = author.find(
            "atom:name",
            namespace
        ).text.strip()

        authors.append(name)

    authors_str = ", ".join(authors)

    existing = db.query(Paper).filter(
        Paper.arxiv_id == paper_id
    ).first()

    if existing:
        continue

    paper = Paper(
        arxiv_id=paper_id,
        title=title,
        abstract=abstract,
        authors=authors_str,
        category="cs.LG",
        published=published,
        url=paper_id
    )

    db.add(paper)

db.commit()

print("Finished ingesting papers.")
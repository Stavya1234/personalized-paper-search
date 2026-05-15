# Personalized Paper Search Engine

A production-style research paper search engine that combines semantic retrieval, lexical search, and personalized ranking to surface relevant arXiv papers.

Built using FastAPI, Sentence Transformers, FAISS, and BM25.

---

# Features

* Semantic search using transformer embeddings
* BM25 lexical retrieval for keyword relevance
* Hybrid ranking pipeline combining semantic + lexical scores
* Personalized ranking using user preference signals
* FastAPI backend with interactive API documentation
* arXiv ingestion pipeline with persistent SQLite storage

---

# Tech Stack

| Component          | Technology            |
| ------------------ | --------------------- |
| Backend API        | FastAPI               |
| Database           | SQLite + SQLAlchemy   |
| Semantic Retrieval | Sentence Transformers |
| Vector Search      | FAISS                 |
| Lexical Search     | BM25                  |
| Data Source        | arXiv API             |

---

# Architecture

```text
User Query
    ↓
Semantic Embedding Search
    ↓
BM25 Lexical Search
    ↓
Hybrid Score Fusion
    ↓
Personalization Boost
    ↓
Ranked Paper Results
```

---

# Local Setup

## Clone Repository

```bash
git clone <your-repo-url>
cd personalized-paper-search
```

## Create Virtual Environment

### Mac/Linux

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Build Search Corpus

## Ingest Papers

```bash
python -m backend.app.ingestion.ingest_arxiv
```

## Generate Embeddings

```bash
python -m backend.app.embeddings.generate_embeddings
```

---

# Run API

```bash
uvicorn backend.app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Interactive API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Example Request

```http
GET /search?query=llm+agents&preferences=rag,llms&top_k=5
```

Example Response:

```json
{
  "query": "llm agents",
  "results": [
    {
      "title": "Paper Title",
      "score": 0.91,
      "semantic_score": 0.88,
      "lexical_score": 0.79
    }
  ]
}
```

---

# Why This Project

This project demonstrates:

* Information retrieval systems
* Vector similarity search
* NLP embeddings
* Hybrid ranking pipelines
* Backend API engineering
* Personalized recommendation logic
* Production-style ML system design

It moves beyond notebook-based ML projects into scalable search system architecture.

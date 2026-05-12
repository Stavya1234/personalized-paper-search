from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = ROOT_DIR / "data"

DATABASE_PATH = DATA_DIR / "papers.db"

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
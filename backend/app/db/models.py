from sqlalchemy import Column, Integer, String, Text, LargeBinary
from .database import Base


class Paper(Base):
    __tablename__ = "papers"
    id = Column(Integer, primary_key=True, index=True)
    arxiv_id = Column(String, unique=True)
    title = Column(Text)
    abstract = Column(Text)
    authors = Column(Text)
    category = Column(String)
    published = Column(String)
    url = Column(Text)
    embedding = Column(LargeBinary)

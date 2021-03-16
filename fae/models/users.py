from sqlalchemy import Column, BIGINT, DATETIME, String, JSON
from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    created_at = Column(DATETIME)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    social = Column(JSON)
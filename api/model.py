from sqlalchemy import Column, VARCHAR, INTEGER
from sqlalchemy.orm import DeclarativeBase
from uuid import uuid4

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "user"
    id_user = Column(VARCHAR(255), primary_key=True, default=lambda: str(uuid4()))
    name = Column(VARCHAR(255), nullable=False)
    age = Column(INTEGER, nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    phone = Column(VARCHAR(20))



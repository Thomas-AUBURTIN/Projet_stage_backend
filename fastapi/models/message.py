from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base
from datetime import datetime

class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    reponse = Column(String, nullable=False)
    Datecreation = Column(DateTime, nullable=True)

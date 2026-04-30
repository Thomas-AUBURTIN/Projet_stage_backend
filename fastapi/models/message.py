from sqlalchemy import Column, Integer, String, Date
from db.database import Base
from datetime import date

class Message(Base):
    __tablename__ = "tache"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    reponse = Column(String, nullable=False)
    messageDate = Column(Date, nullable=True)

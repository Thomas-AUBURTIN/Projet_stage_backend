
from models.message import Message
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from schemas.message import MessageCreation

def getMessages(db : Session):
    try:
        db_message = db.query(Message).all()
        return db_message
    except SQLAlchemyError:
        raise

def createMessage(m : MessageCreation, db : Session):
    try:
        db_message = Message(
                question = m.question,
                reponse = m.reponse,
                Datecreation = m.Datecreation
                )
        db.add(db_message)
        db.commit()
        db.refresh(db_message)
        return db_message
    

    except SQLAlchemyError as e :
        db.rollback()
        raise


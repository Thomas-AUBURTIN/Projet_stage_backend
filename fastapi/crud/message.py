
from models.message import Message
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from schemas.message import MessageCreation,messageOllama
import requests
import json
from datetime import datetime

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

def message_ollama(m : messageOllama, db : Session):
    try:
        data = {
            "model" : "llama3:latest",
            "messages" : [{"role":"user","content": m.question}],
            "stream" : False
        }
        url ="http://localhost:11434/api/chat"
        response = requests.post(url,json=data)
        response.raise_for_status() 
        response_json = json.loads(response.text)
        ai_reply = response_json["message"]["content"]
        db_message = Message(
                question = m.question,
                reponse = ai_reply,
                Datecreation=datetime.utcnow()
                
                )
        db.add(db_message)
        db.commit()
        db.refresh(db_message)
        return db_message
    
    except SQLAlchemyError as e :
        db.rollback()
        raise






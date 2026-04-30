from fastapi  import FastAPI,Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas.message import MessageCreation
import crud.message
from sqlalchemy.exc import SQLAlchemyError

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title = "API de gestion d'historique",
              description="stock et renvoie l'historique des demande")

@app.get("/taches/",
         summary="Récupérer toutes les messages",
         description="Toutes les messages de la table tache se retrouvent dans un JSON",
         response_description="Liste de toutes les tâches au format JSON")                                                                                                        
def getAllMessage(db : Session = Depends(get_db)):
    try: 
        db_message = crud.message.getMessages(db)
    except Exception as e:
        return {"erreur": str(e)}
    return db_message

@app.post("/taches/")
def create_tache(m: MessageCreation, db: Session = Depends(get_db)):
    try:
        return crud.message.createMessage(m,db)
    except Exception as e:
        return {"erreur": str(e)}